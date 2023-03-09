from .request import HaloRequest
from ..exceptions import *


class Login:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def client_credentials_login(self, refresh=False):
        return ClientCredentialsLogin(self.pyhalo, refresh).login()


class ClientCredentialsLogin(HaloRequest):

    def __init__(self, pyhalo, refresh=False):
        super(ClientCredentialsLogin, self).__init__(pyhalo)
        self.refresh = refresh

    def get_endpoint(self):
        endpoint = 'https://{domain}/auth/token' if not self.pyhalo.hosted else 'https://{domain}/auth/token?tenant={tenant}'
        return endpoint.format(domain=self.pyhalo.domain, tenant=self.pyhalo.tenant)

    def get_headers(self):
        return {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }

    def get_body(self):
        if self.refresh:
            return {
                'grant_type': 'refresh_token',
                'client_id': self.pyhalo.client_id,
                'refresh_token': self.pyhalo.refresh_token,
                'scope': self.pyhalo.scope
            }
        else:
            return {
                'grant_type': 'client_credentials',
                'client_id': self.pyhalo.client_id,
                'client_secret': self.pyhalo.client_secret,
                'scope': self.pyhalo.scope
            }

    def login(self):
        try:
            json_response = self.post(self.get_body())
        except HaloRequestFailed as e:
            raise HaloAuthenticationFailed(e.code, e.message)

        access_token = json_response.get('access_token')
        refresh_token = json_response.get('refresh_token')
        id_token = json_response.get('id_token')
        expires_in = json_response.get('expires_in')
        token_type = json_response.get('token_type')
        scope = json_response.get('scope')

        return access_token, refresh_token, id_token, expires_in, token_type, scope
