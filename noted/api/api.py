from django.http import HttpResponse;



def viewApi(request):
	return HttpResponse("Viewing API", content_type = "text/plain");