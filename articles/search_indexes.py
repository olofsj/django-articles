from haystack.indexes import *
from haystack import site
from articles.models import Article


class ArticleIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    author = CharField(model_attr='author')
    pub_date = DateTimeField(model_attr='publish_date')
    rendered = CharField(use_template=True, indexed=False)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Article.objects.filter(status__is_live=True)


site.register(Article, ArticleIndex)
