from .request import HaloRequest


class TicketTypes:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_ticket_types(self, **kwargs):
        return GetTicketTypes(self.pyhalo).get(**kwargs)

    def get_ticket_type(self, ticket_type_id, **kwargs):
        return GetTicketType(self.pyhalo, ticket_type_id).get(**kwargs)

    def post_ticket_type(self, data):
        return PostTicketType(self.pyhalo).post(data)

    def delete_ticket_type(self, ticket_type_id):
        return DeleteTicketType(self.pyhalo, ticket_type_id).delete()


class GetTicketTypes(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/TicketType'.format(domain=self.pyhalo.domain)


class GetTicketType(HaloRequest):
    def __init__(self, pyhalo, ticket_type_id):
        super(GetTicketType, self).__init__(pyhalo)
        self.ticket_type_id = ticket_type_id

    def get_endpoint(self):
        return 'https://{domain}/api/TicketType/{id}'.format(domain=self.pyhalo.domain, id=self.ticket_type_id)


class PostTicketType(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/TicketType'.format(domain=self.pyhalo.domain)


class DeleteTicketType(HaloRequest):
    def __init__(self, pyhalo, ticket_type_id):
        super(DeleteTicketType, self).__init__(pyhalo)
        self.ticket_type_id = ticket_type_id

    def get_endpoint(self):
        return 'https://{domain}/api/TicketType/{id}'.format(domain=self.pyhalo.domain, id=self.ticket_type_id)
