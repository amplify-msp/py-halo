from .request import HaloRequest


class Items:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_items(self, **kwargs):
        return GetItems(self.pyhalo).get(**kwargs)

    def get_item(self, item_id, **kwargs):
        return GetItem(self.pyhalo, item_id).get(**kwargs)

    def post_item(self, data):
        return PostItem(self.pyhalo).post(data)

    def delete_item(self, item_id):
        return DeleteItem(self.pyhalo, item_id).delete()


class GetItems(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Item'.format(domain=self.pyhalo.domain)


class GetItem(HaloRequest):
    def __init__(self, pyhalo, item_id):
        super(GetItem, self).__init__(pyhalo)
        self.item_id = item_id

    def get_endpoint(self):
        return 'https://{domain}/api/Item/{id}'.format(domain=self.pyhalo.domain, id=self.item_id)


class PostItem(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Item'.format(domain=self.pyhalo.domain)


class DeleteItem(HaloRequest):
    def __init__(self, pyhalo, item_id):
        super(DeleteItem, self).__init__(pyhalo)
        self.item_id = item_id

    def get_endpoint(self):
        return 'https://{domain}/api/Item/{id}'.format(domain=self.pyhalo.domain, id=self.item_id)
