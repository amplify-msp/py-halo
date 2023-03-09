from .request import HaloRequest


class Projects:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_projects(self, **kwargs):
        return GetProjects(self.pyhalo).get(**kwargs)

    def get_project(self, project_id, **kwargs):
        return GetProject(self.pyhalo, project_id).get(**kwargs)

    def post_project(self, data):
        return PostProject(self.pyhalo).post(data)

    def delete_project(self, project_id):
        return DeleteProject(self.pyhalo, project_id).delete()


class GetProjects(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Projects'.format(domain=self.pyhalo.domain)


class GetProject(HaloRequest):
    def __init__(self, pyhalo, project_id):
        super(GetProject, self).__init__(pyhalo)
        self.project_id = project_id

    def get_endpoint(self):
        return 'https://{domain}/api/Projects/{id}'.format(domain=self.pyhalo.domain, id=self.project_id)


class PostProject(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Projects'.format(domain=self.pyhalo.domain)


class DeleteProject(HaloRequest):
    def __init__(self, pyhalo, project_id):
        super(DeleteProject, self).__init__(pyhalo)
        self.project_id = project_id

    def get_endpoint(self):
        return 'https://{domain}/api/Projects/{id}'.format(domain=self.pyhalo.domain, id=self.project_id)
