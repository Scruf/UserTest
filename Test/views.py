from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
	index_template = loader.get_template('Test/index.html')
	return HttpResponse(index_template.render(None,request))

def validate(request):
	if request.method == 'POST':
		return HttpResponse("You Poster AssWipe")