from .request import HaloRequest


class Clients:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_clients(self, **kwargs):
        return GetClients(self.pyhalo).get(**kwargs)

    def get_client(self, client_id, **kwargs):
        return GetClient(self.pyhalo, client_id).get(**kwargs)

    def post_client(self, data):
        return PostClient(self.pyhalo).post(data)

    def delete_client(self, client_id):
        return DeleteClient(self.pyhalo, client_id).delete()


class GetClients(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Client'.format(domain=self.pyhalo.domain)


class GetClient(HaloRequest):
    def __init__(self, pyhalo, client_id):
        super(GetClient, self).__init__(pyhalo)
        self.client_id = client_id

    def get_endpoint(self):
        return 'https://{domain}/api/Client/{id}'.format(domain=self.pyhalo.domain, id=self.client_id)


class PostClient(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Client'.format(domain=self.pyhalo.domain)


class DeleteClient(HaloRequest):
    def __init__(self, pyhalo, client_id):
        super(DeleteClient, self).__init__(pyhalo)
        self.client_id = client_id

    def get_endpoint(self):
        return 'https://{domain}/api/Client/{id}'.format(domain=self.pyhalo.domain, id=self.client_id)
