import requests

from django.conf import settings


class ApiClient:
    def __init__(self):
        self.session = requests.Session()

    def _request(self, method, data=None, params=None, **kwargs):
        url_params = {}.update(params or {})
        response = self.session.request(
            method, settings.ENDPOINT_URL, data=data, params=url_params, **kwargs
        )
        return response

    def decode(self, input_str):
        return self._request("get", params={"input": input_str})
