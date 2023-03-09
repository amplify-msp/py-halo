
class HaloError(Exception):

    message = 'Unknown error occurred for {url}. Response content: {content}'

    def __init__(self, url, status, resource_name, content):
        self.url = url
        self.status = status
        self.resource_name = resource_name
        self.content = content

    def __str__(self):
        return self.message.format(url=self.url, content=self.content)

    def __unicode__(self):
        return self.__str__()


class HaloRequestFailed(HaloError):

    message = 'Halo Request Failed. {code}: {err}'

    def __init__(self, code, err):
        self.code = code
        self.err = err if not err else 'No Content'

    def __str__(self):
        return self.message.format(code=self.code, err=self.err)


class HaloAuthenticationFailed(HaloError):

    message = 'Halo Authentication Failed. {code}: {err}'

    def __init__(self, code, err):
        self.code = code
        self.err = err if not err else 'No Content'

    def __str__(self):
        return self.message.format(code=self.code, err=self.err)
