from django.conf.urls import patterns, include, url;
from django.core.urlresolvers import reverse;
from django.contrib import admin;



admin.autodiscover();


from django.http import HttpResponseRedirect;
def redirect(request):
	return HttpResponseRedirect(reverse("noted:index"));




urlpatterns = patterns("",
	url(r"^admin/", include(admin.site.urls)),
	url(r"^noted/", include("noted.urls", namespace = "noted")),
	url(r"^/?$", redirect)
);



import settings;
if (settings.DEBUG):
	urlpatterns += patterns("django.views.static", (r"media/(?P<path>.*)", "serve", {"document_root": settings.MEDIA_ROOT}), );