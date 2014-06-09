import json;
from django.http import HttpResponse;
from django.views.generic.base import View;
from django.utils.decorators import method_decorator;



def isInteger(x):
	return isinstance(x, (int, long));



def toInteger(x):
	try:
		val = int(x);
		return val;
	except ValueError:
		return None;



def returnHttpJson(viewFunction):
	def innerFunction(*args, **kwargs):
		jsonObject = viewFunction(*args, **kwargs);

		if (isInteger(jsonObject)):
			return HttpResponseRedirect("/");

		jsonString = json.dumps(jsonObject, indent = 4);
		return HttpResponse(jsonString, content_type = "application/json");

	return innerFunction;




def viewApi(request):
	return HttpResponse("Viewing API", content_type = "text/plain");




class GetAllNotes(View):
	@method_decorator(returnHttpJson)
	def get(self, request):
		return {
			"notes": [
				{
					"id": 1,
					"user": "Ben",
					"body": "Stuff"
				}, {
					"id": 2,
					"user": "Ben",
					"body": "More stuff"
				}
			]
		};