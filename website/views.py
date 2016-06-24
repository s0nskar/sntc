from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *

def home(request):
	context = {}
	clubs = Club.objects.exclude(slug='sntc')
	secys = Secy.objects.filter(club__slug='sntc').order_by('order')
	topics = SubTopic.objects.filter(club__slug='sntc').order_by('order')
	context['clubs'] = clubs
	context['secys'] = secys
	context['topics'] = topics
	return render(request, 'index.html', context)

def club(request, slug):
	context = {}
	try:
		club = Club.objects.get(slug=slug)
		topics = SubTopic.objects.filter(club__slug=slug).order_by('order')
		secys = Secy.objects.filter(club__slug=slug).order_by('order')
	except:
		return HttpResponse("Some Error 404")
	context['club'] = club
	context['topics'] = topics
	context['secys'] = secys
	return render(request, 'sae.html', context)

@csrf_exempt
def subscribe(request):
	if request.method == "POST":
		email = request.POST['email']
		Subscribe.objects.create(email=email)
		return HttpResponse("{'success':True}")
