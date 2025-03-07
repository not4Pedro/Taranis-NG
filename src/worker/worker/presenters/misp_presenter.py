import os
from base64 import b64encode
import jinja2

from .base_presenter import BasePresenter


class MISPPresenter(BasePresenter):
    type = "MISP_PRESENTER"
    name = "MISP Presenter"
    description = "Presenter for generating MISP platform"

    def generate(self, presenter_input):
        try:
            head, tail = os.path.split(presenter_input.parameter_values_map["MISP_TEMPLATE_PATH"])

            input_data = BasePresenter.generate_input_data(presenter_input)

            env = jinja2.Environment(loader=jinja2.FileSystemLoader(head))

            output_text = env.get_template(tail).render(data=input_data).encode()

            base64_bytes = b64encode(output_text)

            data = base64_bytes.decode("UTF-8")

            return {"mime_type": "application/json", "data": data}
        except Exception as error:
            BasePresenter.print_exception(self, error)
