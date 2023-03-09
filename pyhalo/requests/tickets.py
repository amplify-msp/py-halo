from .request import HaloRequest


class Tickets:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_tickets(self, **kwargs):
        return GetTickets(self.pyhalo).get(**kwargs)

    def get_ticket(self, ticket_id, **kwargs):
        return GetTicket(self.pyhalo, ticket_id).get(**kwargs)

    def post_ticket(self, data):
        return PostTicket(self.pyhalo).post(data)

    def delete_ticket(self, ticket_id, **kwargs):
        return DeleteTicket(self.pyhalo, ticket_id).delete(**kwargs)


class GetTickets(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Tickets'.format(domain=self.pyhalo.domain)


class GetTicket(HaloRequest):
    def __init__(self, pyhalo, ticket_id):
        super(GetTicket, self).__init__(pyhalo)
        self.ticket_id = ticket_id

    def get_endpoint(self):
        return 'https://{domain}/api/Tickets/{id}'.format(domain=self.pyhalo.domain, id=self.ticket_id)


class PostTicket(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Tickets'.format(domain=self.pyhalo.domain)


class DeleteTicket(HaloRequest):
    def __init__(self, pyhalo, ticket_id):
        super(DeleteTicket, self).__init__(pyhalo)
        self.ticket_id = ticket_id

    def get_endpoint(self):
        return 'https://{domain}/api/Tickets/{id}'.format(domain=self.pyhalo.domain, id=self.ticket_id)
