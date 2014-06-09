from django.conf.urls import patterns, url;
from noted.api import api;



urlpatterns = patterns("",
	url(r"^/?$", api.viewApi),
	url(r"^get-all-notes/$", api.GetAllNotes.as_view()),
);