from django.conf.urls import patterns, url;
from noted.api import api;



urlpatterns = patterns("",
	url(r"^/?$", api.viewApi),
);