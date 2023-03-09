from .request import HaloRequest


class Attachments:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_attachments(self, **kwargs):
        return GetAttachments(self.pyhalo).get(**kwargs)

    def get_attachment(self, attachment_id, **kwargs):
        return GetAttachment(self.pyhalo, attachment_id).get(**kwargs)

    def post_attachment(self, data):
        return PostAttachment(self.pyhalo).post(data)

    def delete_attachment(self, attachment_id):
        return DeleteAttachment(self.pyhalo, attachment_id).delete()


class GetAttachments(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Attachment'.format(domain=self.pyhalo.domain)


class GetAttachment(HaloRequest):
    def __init__(self, pyhalo, attachment_id):
        super(GetAttachment, self).__init__(pyhalo)
        self.attachment_id = attachment_id

    def get_endpoint(self):
        return 'https://{domain}/api/Attachment/{id}'.format(domain=self.pyhalo.domain, id=self.attachment_id)


class PostAttachment(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/Attachment'.format(domain=self.pyhalo.domain)


class DeleteAttachment(HaloRequest):
    def __init__(self, pyhalo, attachment_id):
        super(DeleteAttachment, self).__init__(pyhalo)
        self.attachment_id = attachment_id

    def get_endpoint(self):
        return 'https://{domain}/api/Attachment/{id}'.format(domain=self.pyhalo.domain, id=self.attachment_id)
