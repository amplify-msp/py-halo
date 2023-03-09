from .request import HaloRequest


class Users:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_users(self, **kwargs):
        return GetUsers(self.pyhalo).get(**kwargs)

    def get_user(self, user_id, **kwargs):
        return GetUser(self.pyhalo, user_id).get(**kwargs)

    def post_user(self, data):
        return PostUser(self.pyhalo).post(data)

    def delete_user(self, user_id):
        return DeleteUser(self.pyhalo, user_id).delete()


class GetUsers(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Users'.format(domain=self.pyhalo.domain)


class GetUser(HaloRequest):
    def __init__(self, pyhalo, user_id):
        super(GetUser, self).__init__(pyhalo)
        self.user_id = user_id

    def get_endpoint(self):
        return 'https://{domain}/api/Users/{id}'.format(domain=self.pyhalo.domain, id=self.user_id)


class PostUser(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Users'.format(domain=self.pyhalo.domain)


class DeleteUser(HaloRequest):
    def __init__(self, pyhalo, user_id):
        super(DeleteUser, self).__init__(pyhalo)
        self.user_id = user_id

    def get_endpoint(self):
        return 'https://{domain}/api/Users/{id}'.format(domain=self.pyhalo.domain, id=self.user_id)
