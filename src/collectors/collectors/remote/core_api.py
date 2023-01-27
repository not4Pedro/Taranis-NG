import urllib
import requests
import base64
from urllib.parse import quote
from collectors.managers.log_manager import logger
from collectors.config import Config


class CoreApi:
    def __init__(self):
        self.api_url = Config.TARANIS_NG_CORE_URL
        self.api_key = Config.API_KEY
        self.headers = self.get_headers()
        self.node_id = self.get_node_id()
        self.verify = Config.SSL_VERIFICATION

    def get_headers(self) -> dict:
        return {"Authorization": f"Bearer {self.api_key}", "Content-type": "application/json"}

    def get_node_id(self) -> str:
        uid = self.api_url + self.api_key
        return base64.urlsafe_b64encode(uid.encode("utf-8")).decode("utf-8")

    def get_osint_sources(self, collector_type):
        try:
            response = requests.get(
                f"{self.api_url}/api/v1/collectors/osint-sources/{quote(collector_type)}",
                headers=self.headers,
                verify=self.verify,
            )

            return response.json(), response.status_code
        except Exception:
            logger.log_debug_trace("Can't get OSINT Sources")
            return None, 400

    def register_node(self):
        try:
            response = self.get_collector_status()
            if response:
                logger.log_info(f"Found registerd Collector {response}")
                return

            logger.log_debug(f"Registering Collector Node at {Config.TARANIS_NG_CORE_URL}")
            node_info = {
                "id": self.node_id,
                "name": Config.NODE_NAME,
                "description": Config.NODE_DESCRIPTION,
                "api_url": Config.NODE_URL,
                "api_key": Config.API_KEY,
            }

            response = requests.post(
                f"{self.api_url}/api/v1/collectors/node",
                json=node_info,
                headers=self.headers,
                verify=self.verify,
            )

            if response.ok:
                logger.log_info(f"Successfully registered: {response}")
            else:
                logger.critical(f"Can't register Collector node: {response.text}")

        except Exception:
            logger.log_debug_trace("Can't register Collector node")

    def get_collector_status(self) -> dict|None:
        try:
            response = requests.get(f"{self.api_url}/api/v1/collectors/node/{self.node_id}", headers=self.headers, verify=self.verify)
            return response.json() if response.ok else None
        except Exception:
            logger.log_debug_trace("Cannot update Collector status")
            return None

    def add_news_items(self, news_items):
        try:
            response = requests.post(
                f"{self.api_url}/api/v1/collectors/news-items", json=news_items, headers=self.headers, verify=self.verify
            )

            return response.status_code
        except Exception:
            logger.log_debug_trace("Cannot add Newsitem")
            return None, 400
