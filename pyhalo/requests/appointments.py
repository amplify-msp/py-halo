from .request import HaloRequest


class Appointments:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_appointments(self, **kwargs):
        return GetAppointments(self.pyhalo).get(**kwargs)

    def get_appointment(self, app_id, **kwargs):
        return GetAppointment(self.pyhalo, app_id).get(**kwargs)

    def post_appointment(self, data):
        return PostAppointment(self.pyhalo).post(data)

    def delete_appointment(self, app_id):
        return DeleteAppointment(self.pyhalo, app_id).delete()


class GetAppointments(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Appointment'.format(domain=self.pyhalo.domain)


class GetAppointment(HaloRequest):
    def __init__(self, pyhalo, app_id):
        super(GetAppointment, self).__init__(pyhalo)
        self.app_id = app_id

    def get_endpoint(self):
        return 'https://{domain}/api/Appointment/{id}'.format(domain=self.pyhalo.domain, id=self.app_id)


class PostAppointment(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Appointment'.format(domain=self.pyhalo.domain)


class DeleteAppointment(HaloRequest):
    def __init__(self, pyhalo, app_id):
        super(DeleteAppointment, self).__init__(pyhalo)
        self.app_id = app_id

    def get_endpoint(self):
        return 'https://{domain}/api/Appointment/{id}'.format(domain=self.pyhalo.domain, id=self.app_id)
