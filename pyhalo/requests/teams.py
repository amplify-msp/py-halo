from .request import HaloRequest


class Teams:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_teams(self, **kwargs):
        return GetTeams(self.pyhalo).get(**kwargs)

    def get_team(self, team_id, **kwargs):
        return GetTeam(self.pyhalo, team_id).get(**kwargs)

    def post_team(self, data):
        return PostTeam(self.pyhalo).post(data)

    def delete_team(self, team_id):
        return DeleteTeam(self.pyhalo, team_id).delete()


class GetTeams(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Team'.format(domain=self.pyhalo.domain)


class GetTeam(HaloRequest):
    def __init__(self, pyhalo, team_id):
        super(GetTeam, self).__init__(pyhalo)
        self.team_id = team_id

    def get_endpoint(self):
        return 'https://{domain}/api/Team/{id}'.format(domain=self.pyhalo.domain, id=self.team_id)


class PostTeam(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Team'.format(domain=self.pyhalo.domain)


class DeleteTeam(HaloRequest):
    def __init__(self, pyhalo, team_id):
        super(DeleteTeam, self).__init__(pyhalo)
        self.team_id = team_id

    def get_endpoint(self):
        return 'https://{domain}/api/Team/{id}'.format(domain=self.pyhalo.domain, id=self.team_id)
