from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):
	return render(request, 'index.html', {})

def amc(request):
	return render(request, 'amc.html', {})

def astro(request):
	return render(request, 'astro.html', {})

def cops(request):
	return render(request, 'cops.html', {})

def green(request):
	return render(request, 'green.html', {})

def out(request):
	return render(request, 'out.html', {})

def robo(request):
	return render(request, 'robo.html', {})

def sae(request):
	return render(request, 'sae.html', {})

def user(request):
	 User.objects.create_superuser('admin', 'admin@example.com', 'iamadmin')
	 return HttpResponse("Done")
