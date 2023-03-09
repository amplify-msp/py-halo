import logging
import requests
from datetime import datetime, timedelta
from .requests import *

logger = logging.getLogger(__name__)


class PyHalo:

    def __init__(
            self,
            client_id=None,
            client_secret=None,
            scope=None,
            domain=None,
            tenant=None,
            hosted=False,
            session=None,
            proxies=None
    ):
        self.client_id = client_id
        self.client_secret = client_secret

        self.scope = scope
        if self.scope is None:
            self.scope = 'all'

        self.domain = domain
        if self.domain is None:
            self.domain = 'support.haloservicedesk.com'

        self.tenant = tenant
        self.hosted = hosted
        self.session = session or requests.Session()
        self.proxies = self.session.proxies
        self.access_token = None
        self.refresh_token = None
        self.id_token = None
        self.expires_in = None
        self.expires = None
        self.token_type = None

        if proxies is not None:
            if not session:
                self.session.proxies = self.proxies = proxies
            else:
                logger.warning(
                    'Proxies must be defined on custom session object, '
                    'ignoring proxies: %s', proxies
                )

        self.perform_login()

    def perform_login(self, refresh=False):
        logger.debug('Performing Login')
        self.expires = datetime.now()
        self.access_token, self.refresh_token, self.id_token, self.expires_in, self.token_type, self.scope = self.login().client_credentials_login(refresh)
        self.expires = self.expires + timedelta(seconds=self.expires_in)
        logger.info(f'Login successful. Session active until {self.expires}')

    def check_expires(self):
        if datetime.now() > self.expires:
            logger.info('Login Expired - refreshing tokens')
            self.perform_login(True)

    def actions(self):
        return Actions(self)

    def agents(self):
        return Agents(self)

    def appointments(self):
        return Appointments(self)

    def assets(self):
        return Assets(self)

    def attachments(self):
        return Attachments(self)

    def clients(self):
        return Clients(self)

    def contracts(self):
        return Contracts(self)

    def invoices(self):
        return Invoices(self)

    def items(self):
        return Items(self)

    def knowledge_base(self):
        return KnowledgeBase(self)

    def opportunities(self):
        return Opportunities(self)

    def quotes(self):
        return Quotes(self)

    def reports(self):
        return Reports(self)

    def sites(self):
        return Sites(self)

    def status(self):
        return Status(self)

    def suppliers(self):
        return Suppliers(self)

    def teams(self):
        return Teams(self)

    def ticket_types(self):
        return TicketTypes(self)

    def login(self):
        return Login(self)

    def tickets(self):
        return Tickets(self)

    def users(self):
        return Users(self)

