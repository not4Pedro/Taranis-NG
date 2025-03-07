from celery import Celery
from flask import Flask

from core.managers.log_manager import logger
from core.model.queue import ScheduleEntry
from kombu.exceptions import OperationalError

queue_manager: "QueueManager"
periodic_tasks = [
    {"id": "cleanup_token_blacklist", "task": "worker.tasks.cleanup_token_blacklist", "schedule": "daily", "args": []},
]


class QueueManager:
    def __init__(self, app: Flask):
        self.celery: Celery = self.init_app(app)
        self.error: str = ""

    def init_app(self, app: Flask):
        celery_app = Celery(app.name)
        celery_app.config_from_object(app.config["CELERY"])
        celery_app.set_default()
        app.extensions["celery"] = celery_app
        return celery_app

    def post_init(self):
        self.add_periodic_tasks()
        self.update_task_queue_from_osint_sources()
        self.schedule_word_list_gathering()

    def add_periodic_tasks(self):
        for task in periodic_tasks:
            ScheduleEntry.add_or_update(task)

    def update_task_queue_from_osint_sources(self):
        from core.model.osint_source import OSINTSource

        sources = OSINTSource.get_all()
        for source in sources:
            ScheduleEntry.add_or_update(source.to_task_dict())

    def schedule_word_list_gathering(self):
        from core.model.word_list import WordList

        word_lists = WordList.get_all_empty()
        for word_list in word_lists:
            logger.debug(f"Schedule gathering for WordList {word_list.id}")
            self.celery.send_task("worker.tasks.gather_word_list", args=[word_list.id], task_id=f"gather_word_list_{word_list.id}")

    def ping_workers(self):
        if self.error:
            logger.error("QueueManager not initialized")
            return {"error": "QueueManager not initialized"}, 500
        try:
            result = self.celery.control.ping()
            self.error = ""
            return [
                {
                    "name": list(worker.keys())[0],
                    "status": list(list(worker.values())[0].keys())[0],
                }
                for worker in result
            ]
        except Exception:
            self.error = "Could not reach rabbitmq"
            return {"error": "Could not reach rabbitmq"}, 500

    def send_task(self, *args, **kwargs):
        if self.error:
            return False
        self.celery.send_task(*args, **kwargs)
        return True

    def get_queue_status(self) -> tuple[dict, int]:
        if self.error:
            return {"error": "Could not reach rabbitmq", "url": ""}, 500
        return {"status": "🚀 Up and running 🏃", "url": f"{queue_manager.celery.broker_connection().as_uri()}"}, 200

    def collect_osint_source(self, source_id: str):
        if self.send_task("worker.tasks.collect", args=[source_id]):
            logger.info(f"Collect for source {source_id} scheduled")
            return {"message": f"Refresh for source {source_id} scheduled"}, 200
        return {"error": "Could not reach rabbitmq"}, 500

    def collect_all_osint_sources(self):
        from core.model.osint_source import OSINTSource

        if self.error:
            return {"error": "Could not reach rabbitmq"}, 500
        sources = OSINTSource.get_all()
        for source in sources:
            self.send_task("worker.tasks.collect", args=[source.id])
            logger.info(f"Collect for source {source.id} scheduled")
        return {"message": f"Refresh for source {len(sources)} scheduled"}, 200

    def gather_word_list(self, word_list_id: int):
        if self.send_task("worker.tasks.gather_word_list", args=[word_list_id]):
            logger.info(f"Gathering for WordList {word_list_id} scheduled")
            return {"message": f"Gathering for WordList {word_list_id} scheduled"}, 200
        return {"error": "Could not reach rabbitmq"}, 500

    def execute_bot_task(self, bot_id: int):
        if self.send_task("worker.tasks.execute_bot", args=[bot_id]):
            logger.info(f"Executing Bot {bot_id} scheduled")
            return {"message": f"Executing Bot {bot_id} scheduled"}, 200
        return {"error": "Could not reach rabbitmq"}, 500


def initialize(app: Flask, first_worker: bool):
    global queue_manager
    queue_manager = QueueManager(app)
    try:
        with queue_manager.celery.connection() as conn:
            conn.ensure_connection(max_retries=3)
            queue_manager.error = ""
        if first_worker:
            logger.info(f"QueueManager initialized: {queue_manager.celery.broker_connection().as_uri()}")
            queue_manager.post_init()
    except OperationalError:
        logger.error("Could not reach rabbitmq")
        queue_manager.error = "Could not reach rabbitmq"
    except Exception:
        logger.exception()
        queue_manager.error = "Could not reach rabbitmq"
