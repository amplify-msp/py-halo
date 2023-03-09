import logging
import requests
from json.decoder import JSONDecodeError
from ..exceptions import HaloRequestFailed

logger = logging.getLogger(__name__)


class HaloRequest:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_endpoint(self):
        raise NotImplementedError('Request require get_endpoint')

    def get_headers(self):
        return {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.pyhalo.access_token}'
        }

    def get_body(self):
        return {}

    def handle_response(self, response):
        if response.status_code != 200:
            raise HaloRequestFailed(response.status_code, response.text)

        try:
            json_response = response.json()
        except JSONDecodeError:
            raise HaloRequestFailed(
                response.status_code, response.text
            )

        return json_response

    def get(self, **kwargs):
        response = (self.pyhalo.session or requests).get(
            self.get_endpoint(),
            params=kwargs,
            headers=self.get_headers(),
            proxies=self.pyhalo.proxies
        )

        return self.handle_response(response)

    def post(self, data):
        response = (self.pyhalo.session or requests).post(
            self.get_endpoint(),
            data,
            headers=self.get_headers(),
            proxies=self.pyhalo.proxies
        )
        return self.handle_response(response)

    def delete(self, **kwargs):
        response = (self.pyhalo.session or requests).delete(
            self.get_endpoint(),
            params=kwargs,
            headers=self.get_headers(),
            proxies=self.pyhalo.proxies
        )
        return self.handle_response(response)

