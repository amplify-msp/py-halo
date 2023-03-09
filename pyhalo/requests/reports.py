from .request import HaloRequest


class Reports:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_reports(self, **kwargs):
        return GetReports(self.pyhalo).get(**kwargs)

    def get_report(self, report_id, **kwargs):
        return GetReport(self.pyhalo, report_id).get(**kwargs)

    def post_report(self, data):
        return PostReport(self.pyhalo).post(data)

    def delete_report(self, report_id):
        return DeleteReport(self.pyhalo, report_id).delete()


class GetReports(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Report'.format(domain=self.pyhalo.domain)


class GetReport(HaloRequest):
    def __init__(self, pyhalo, report_id):
        super(GetReport, self).__init__(pyhalo)
        self.report_id = report_id

    def get_endpoint(self):
        return 'https://{domain}/api/Report/{id}'.format(domain=self.pyhalo.domain, id=self.report_id)


class PostReport(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Report'.format(domain=self.pyhalo.domain)


class DeleteReport(HaloRequest):
    def __init__(self, pyhalo, report_id):
        super(DeleteReport, self).__init__(pyhalo)
        self.report_id = report_id

    def get_endpoint(self):
        return 'https://{domain}/api/Report/{id}'.format(domain=self.pyhalo.domain, id=self.report_id)
