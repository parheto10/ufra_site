from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostFeed(Feed):
    titre = 'Mon Blog'
    link = '/'
    description = 'Nouveau articles de postes.'

    def items(self):
        return Post.publier.all()[:5]

    def item_title(self, item):
        return item.titre

    def item_description(self, item):
        return truncatewords(item.message, 30)