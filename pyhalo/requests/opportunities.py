from .request import HaloRequest


class Opportunities:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_opportunities(self, **kwargs):
        return GetOpportunities(self.pyhalo).get(**kwargs)

    def get_opportunity(self, opportunity_id, **kwargs):
        return GetOpportunity(self.pyhalo, opportunity_id).get(**kwargs)

    def post_opportunity(self, data):
        return PostOpportunity(self.pyhalo).post(data)

    def delete_opportunity(self, opportunity_id):
        return DeleteOpportunity(self.pyhalo, opportunity_id).delete()


class GetOpportunities(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Opportunities'.format(domain=self.pyhalo.domain)


class GetOpportunity(HaloRequest):
    def __init__(self, pyhalo, opportunity_id):
        super(GetOpportunity, self).__init__(pyhalo)
        self.opportunity_id = opportunity_id

    def get_endpoint(self):
        return 'https://{domain}/api/Opportunities/{id}'.format(domain=self.pyhalo.domain, id=self.opportunity_id)


class PostOpportunity(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Opportunities'.format(domain=self.pyhalo.domain)


class DeleteOpportunity(HaloRequest):
    def __init__(self, pyhalo, opportunity_id):
        super(DeleteOpportunity, self).__init__(pyhalo)
        self.opportunity_id = opportunity_id

    def get_endpoint(self):
        return 'https://{domain}/api/Opportunities/{id}'.format(domain=self.pyhalo.domain, id=self.opportunity_id)
