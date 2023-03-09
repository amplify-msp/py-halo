from .request import HaloRequest


class Invoices:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_invoices(self, **kwargs):
        return GetInvoices(self.pyhalo).get(**kwargs)

    def get_invoice(self, invoice_id, **kwargs):
        return GetInvoice(self.pyhalo, invoice_id).get(**kwargs)

    def post_invoice(self, data):
        return PostInvoice(self.pyhalo).post(data)

    def delete_invoice(self, invoice_id):
        return DeleteInvoice(self.pyhalo, invoice_id).delete()


class GetInvoices(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Invoice'.format(domain=self.pyhalo.domain)


class GetInvoice(HaloRequest):
    def __init__(self, pyhalo, invoice_id):
        super(GetInvoice, self).__init__(pyhalo)
        self.invoice_id = invoice_id

    def get_endpoint(self):
        return 'https://{domain}/api/Invoice/{id}'.format(domain=self.pyhalo.domain, id=self.invoice_id)


class PostInvoice(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Invoice'.format(domain=self.pyhalo.domain)


class DeleteInvoice(HaloRequest):
    def __init__(self, pyhalo, invoice_id):
        super(DeleteInvoice, self).__init__(pyhalo)
        self.invoice_id = invoice_id

    def get_endpoint(self):
        return 'https://{domain}/api/Invoice/{id}'.format(domain=self.pyhalo.domain, id=self.invoice_id)
