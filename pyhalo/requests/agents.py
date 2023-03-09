from .request import HaloRequest


class Agents:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_agents(self, **kwargs):
        return GetAgents(self.pyhalo).get(**kwargs)

    def get_agent(self, agent_id, **kwargs):
        return GetAgent(self.pyhalo, agent_id).get(**kwargs)

    def get_me(self):
        return GetAgent(self.pyhalo, 'me').get()

    def post_agent(self, data):
        return PostAgent(self.pyhalo).post(data)

    def delete_agent(self, agent_id):
        return DeleteAgent(self.pyhalo, agent_id).delete()


class GetAgents(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Agent'.format(domain=self.pyhalo.domain)


class GetAgent(HaloRequest):
    def __init__(self, pyhalo, agent_id):
        super(GetAgent, self).__init__(pyhalo)
        self.agent_id = agent_id

    def get_endpoint(self):
        return 'https://{domain}/api/Agent/{id}'.format(domain=self.pyhalo.domain, id=self.agent_id)


class PostAgent(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Agent'.format(domain=self.pyhalo.domain)


class DeleteAgent(HaloRequest):
    def __init__(self, pyhalo, agent_id):
        super(DeleteAgent, self).__init__(pyhalo)
        self.agent_id = agent_id

    def get_endpoint(self):
        return 'https://{domain}/api/Agent/{id}'.format(domain=self.pyhalo.domain, id=self.agent_id)
