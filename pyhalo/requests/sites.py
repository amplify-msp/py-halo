from .request import HaloRequest


class Sites:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_sites(self, **kwargs):
        return GetSites(self.pyhalo).get(**kwargs)

    def get_site(self, site_id, **kwargs):
        return GetSite(self.pyhalo, site_id).get(**kwargs)

    def post_site(self, data):
        return PostSite(self.pyhalo).post(data)

    def delete_site(self, site_id):
        return DeleteSite(self.pyhalo, site_id).delete()


class GetSites(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Site'.format(domain=self.pyhalo.domain)


class GetSite(HaloRequest):
    def __init__(self, pyhalo, site_id):
        super(GetSite, self).__init__(pyhalo)
        self.site_id = site_id

    def get_endpoint(self):
        return 'https://{domain}/api/Site/{id}'.format(domain=self.pyhalo.domain, id=self.site_id)


class PostSite(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Site'.format(domain=self.pyhalo.domain)


class DeleteSite(HaloRequest):
    def __init__(self, pyhalo, site_id):
        super(DeleteSite, self).__init__(pyhalo)
        self.site_id = site_id

    def get_endpoint(self):
        return 'https://{domain}/api/Site/{id}'.format(domain=self.pyhalo.domain, id=self.site_id)
