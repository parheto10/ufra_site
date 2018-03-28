from django.conf.urls import url
from django.contrib.auth.views import (
	login,
	logout,
	logout_then_login,

)
from .views import user_login, dashboard
urlpatterns = [
	 # login view
	 #url(r'^login/$', user_login, name='connexion'),
	url(r'^$', dashboard, name='dashboard'),
	#login logout
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
]