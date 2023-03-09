from .request import HaloRequest


class Actions:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_actions(self, **kwargs):
        return GetActions(self.pyhalo).get(**kwargs)

    def get_action(self, action_id, **kwargs):
        return GetAction(self.pyhalo, action_id).get(**kwargs)


class GetActions(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Actions'.format(domain=self.pyhalo.domain)


class GetAction(HaloRequest):
    def __init__(self, pyhalo, action_id):
        super(GetAction, self).__init__(pyhalo)
        self.action_id = action_id

    def get_endpoint(self):
        return 'https://{domain}/api/Actions/{id}'.format(domain=self.pyhalo.domain, id=self.action_id)

