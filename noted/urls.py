from django.conf.urls import patterns, include, url;
from noted import views;



urlpatterns = patterns("",
	url(r"^$", views.Index.as_view(), name = "index"),
	url(r"^api/", include("noted.api.urls", namespace = "api"))
);