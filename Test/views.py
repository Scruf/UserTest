from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import User
# Create your views here.
def index(request):
	index_template = loader.get_template('Test/index.html')
	return HttpResponse(index_template.render(None,request))

def validate(request):
	if request.method == 'POST':
<<<<<<< HEAD
		try:
			user = User.objects.get(email=request.POST.get('email'))
			return HttpResponse("Success")
		except User.DoesNotExists:
			return HttpResponse("Failure")
	
=======
	    try:
                user = User.objects.get(email=request.POST.get('email'), password=request.POST.get('password'))
                return HttpResponse('Success')
            except User.DoesNotExists:
                return HttpResponse('Failure')
>>>>>>> 1cc4baba81f875bb9f6270a5f9f1de0ef3913586

def register(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = User(email=email,password=password)
		user.save()
		return redirect ('/')

def save(request):
	save_template = loader.get_template('Test/register.html')
	return HttpResponse(save_template.render(None, request))

