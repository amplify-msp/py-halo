from .request import HaloRequest


class KnowledgeBase:

    def __init__(self, pyhalo):
        self.pyhalo = pyhalo

    def get_articles(self, **kwargs):
        return GetArticles(self.pyhalo).get(**kwargs)

    def get_article(self, article_id, **kwargs):
        return GetArticle(self.pyhalo, article_id).get(**kwargs)

    def post_article(self, data):
        return PostArticle(self.pyhalo).post(data)

    def delete_article(self, article_id):
        return DeleteArticle(self.pyhalo, article_id).delete()


class GetArticles(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/KBArticle'.format(domain=self.pyhalo.domain)


class GetArticle(HaloRequest):
    def __init__(self, pyhalo, article_id):
        super(GetArticle, self).__init__(pyhalo)
        self.article_id = article_id

    def get_endpoint(self):
        return 'https://{domain}/api/KBArticle/{id}'.format(domain=self.pyhalo.domain, id=self.article_id)


class PostArticle(HaloRequest):

    def get_endpoint(self):
        return 'https://{domain}/api/KBArticle'.format(domain=self.pyhalo.domain)


class DeleteArticle(HaloRequest):
    def __init__(self, pyhalo, article_id):
        super(DeleteArticle, self).__init__(pyhalo)
        self.article_id = article_id

    def get_endpoint(self):
        return 'https://{domain}/api/KBArticle/{id}'.format(domain=self.pyhalo.domain, id=self.article_id)
