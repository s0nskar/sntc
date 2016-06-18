from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import *

def home(request):
	context = {}
	clubs = Club.objects.all()
	context['clubs'] = clubs
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
