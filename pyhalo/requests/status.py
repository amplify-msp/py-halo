from .request import HaloRequest


class Status:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_statuses(self, **kwargs):
        return GetStatuses(self.pyhalo).get(**kwargs)

    def get_status(self, status_id, **kwargs):
        return GetStatus(self.pyhalo, status_id).get(**kwargs)

    def post_status(self, data):
        return PostStatus(self.pyhalo).post(data)

    def delete_status(self, status_id):
        return DeleteStatus(self.pyhalo, status_id).delete()


class GetStatuses(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Status'.format(domain=self.pyhalo.domain)


class GetStatus(HaloRequest):
    def __init__(self, pyhalo, status_id):
        super(GetStatus, self).__init__(pyhalo)
        self.status_id = status_id

    def get_endpoint(self):
        return 'https://{domain}/api/Status/{id}'.format(domain=self.pyhalo.domain, id=self.status_id)


class PostStatus(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Status'.format(domain=self.pyhalo.domain)


class DeleteStatus(HaloRequest):
    def __init__(self, pyhalo, status_id):
        super(DeleteStatus, self).__init__(pyhalo)
        self.status_id = status_id

    def get_endpoint(self):
        return 'https://{domain}/api/Status/{id}'.format(domain=self.pyhalo.domain, id=self.status_id)
