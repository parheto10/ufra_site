from django.conf.urls import url
from django.contrib import admin
from .views import post_list, post_detail, partager
from django.utils.translation import gettext_lazy as _

from .feeds import LatestPostFeed

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(_(r'^tag/(?P<tag_slug>[-\w]+)/$'), post_list, name='post_list_by_tag'),
    url(_(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$'), post_detail, name='post_detail'),
    #url(r'^(?P<post_id>\d+)/share/$', partager, name='partager'),
    url(_(r'^(?P<slug>[\w-]+)/partager/$'), partager, name='partager'),
    url(_(r'^feed/$'), LatestPostFeed(), name='post_feed'),
]