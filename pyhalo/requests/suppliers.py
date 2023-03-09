from .request import HaloRequest


class Suppliers:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_suppliers(self, **kwargs):
        return GetSuppliers(self.pyhalo).get(**kwargs)

    def get_supplier(self, supplier_id, **kwargs):
        return GetSupplier(self.pyhalo, supplier_id).get(**kwargs)

    def post_supplier(self, data):
        return PostSupplier(self.pyhalo).post(data)

    def delete_supplier(self, supplier_id):
        return DeleteSupplier(self.pyhalo, supplier_id).delete()


class GetSuppliers(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Supplier'.format(domain=self.pyhalo.domain)


class GetSupplier(HaloRequest):
    def __init__(self, pyhalo, supplier_id):
        super(GetSupplier, self).__init__(pyhalo)
        self.supplier_id = supplier_id

    def get_endpoint(self):
        return 'https://{domain}/api/Supplier/{id}'.format(domain=self.pyhalo.domain, id=self.supplier_id)


class PostSupplier(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Supplier'.format(domain=self.pyhalo.domain)


class DeleteSupplier(HaloRequest):
    def __init__(self, pyhalo, supplier_id):
        super(DeleteSupplier, self).__init__(pyhalo)
        self.supplier_id = supplier_id

    def get_endpoint(self):
        return 'https://{domain}/api/Supplier/{id}'.format(domain=self.pyhalo.domain, id=self.supplier_id)
