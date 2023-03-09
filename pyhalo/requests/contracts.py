from .request import HaloRequest


class Contracts:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_contracts(self, **kwargs):
        return GetContracts(self.pyhalo).get(**kwargs)

    def get_contract(self, contract_id, **kwargs):
        return GetContract(self.pyhalo, contract_id).get(**kwargs)

    def post_contract(self, data):
        return PostContract(self.pyhalo).post(data)

    def delete_contract(self, contract_id):
        return DeleteContract(self.pyhalo, contract_id).delete()


class GetContracts(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/ClientContract'.format(domain=self.pyhalo.domain)


class GetContract(HaloRequest):
    def __init__(self, pyhalo, contract_id):
        super(GetContract, self).__init__(pyhalo)
        self.contract_id = contract_id

    def get_endpoint(self):
        return 'https://{domain}/api/ClientContract/{id}'.format(domain=self.pyhalo.domain, id=self.contract_id)


class PostContract(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/ClientContract'.format(domain=self.pyhalo.domain)


class DeleteContract(HaloRequest):
    def __init__(self, pyhalo, contract_id):
        super(DeleteContract, self).__init__(pyhalo)
        self.contract_id = contract_id

    def get_endpoint(self):
        return 'https://{domain}/api/ClientContract/{id}'.format(domain=self.pyhalo.domain, id=self.contract_id)
