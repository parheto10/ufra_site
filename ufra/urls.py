"""ufra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from posts.sitemaps import PostSitemap
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from .views import (
    erreur_400,
    erreur_403,
    erreur_404,
    erreur_500
)
handler404 = erreur_404 #not_found
handler500 = erreur_500 #server_error
handler403 = erreur_403 #permission_denied
handler400 = erreur_400 #bad_request


sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^compte/', include('compte.urls', namespace='compte', app_name='compte')),
    url(_(r'^posts/'), include('posts.urls', namespace='posts', app_name='posts')),
    url(_(r'^sitemap\.xml$'), sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    url(r'^rosetta/', include('rosetta.urls')),
    url(_(r'^'), include('annonces.urls', namespace='annonces', app_name='annonces')),
)
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
