from .request import HaloRequest


class Quotes:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_quotes(self, **kwargs):
        return GetQuotes(self.pyhalo).get(**kwargs)

    def get_quote(self, quote_id, **kwargs):
        return GetQuote(self.pyhalo, quote_id).get(**kwargs)

    def post_quote(self, data):
        return PostQuote(self.pyhalo).post(data)

    def delete_quote(self, quote_id):
        return DeleteQuote(self.pyhalo, quote_id).delete()


class GetQuotes(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Quotation'.format(domain=self.pyhalo.domain)


class GetQuote(HaloRequest):
    def __init__(self, pyhalo, quote_id):
        super(GetQuote, self).__init__(pyhalo)
        self.quote_id = quote_id

    def get_endpoint(self):
        return 'https://{domain}/api/Quotation/{id}'.format(domain=self.pyhalo.domain, id=self.quote_id)


class PostQuote(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Quotation'.format(domain=self.pyhalo.domain)


class DeleteQuote(HaloRequest):
    def __init__(self, pyhalo, quote_id):
        super(DeleteQuote, self).__init__(pyhalo)
        self.quote_id = quote_id

    def get_endpoint(self):
        return 'https://{domain}/api/Quotation/{id}'.format(domain=self.pyhalo.domain, id=self.quote_id)
