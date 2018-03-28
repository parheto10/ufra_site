# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from .views import index, contact, about, annonces, temoigne, temoignage
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    url(_(r'^$'), index, name='index'),
    url(_(r'^temoigne/$'), temoigne, name='temoigne'),
    url(_(r'^temoignage/$'), temoignage, name='temoignage'),
    url(_(r'^annonces/$'), annonces, name='annonces'),
    url(_(r'^about/$'), about, name='about'),
    url(_(r'^contact/$'), contact, name='contact'),
   # url(r'^(?P<slug>[\w-]+)/$', detail, name='detail'),
]