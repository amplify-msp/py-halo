from .request import HaloRequest


class Assets:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_assets(self, **kwargs):
        return GetAssets(self.pyhalo).get(**kwargs)

    def get_asset(self, asset_id, **kwargs):
        return GetAsset(self.pyhalo, asset_id).get(**kwargs)

    def post_asset(self, data):
        return PostAsset(self.pyhalo).post(data)

    def delete_asset(self, asset_id):
        return DeleteAsset(self.pyhalo, asset_id).delete()


class GetAssets(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Asset'.format(domain=self.pyhalo.domain)


class GetAsset(HaloRequest):
    def __init__(self, pyhalo, asset_id):
        super(GetAsset, self).__init__(pyhalo)
        self.asset_id = asset_id

    def get_endpoint(self):
        return 'https://{domain}/api/Asset/{id}'.format(domain=self.pyhalo.domain, id=self.asset_id)


class PostAsset(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Asset'.format(domain=self.pyhalo.domain)


class DeleteAsset(HaloRequest):
    def __init__(self, pyhalo, asset_id):
        super(DeleteAsset, self).__init__(pyhalo)
        self.asset_id = asset_id

    def get_endpoint(self):
        return 'https://{domain}/api/Asset/{id}'.format(domain=self.pyhalo.domain, id=self.asset_id)
