from __future__ import unicode_literals

from django.db import models

class Club(models.Model):
	name = models.CharField(max_length=30)
	slug = models.SlugField()

	def __unicode__(self):
		return self.name

class SubTopic(models.Model):
	club = models.ForeignKey(Club)
	heading = models.CharField(max_length=20)
	about = models.TextField()
	order = models.IntegerField()

	def __unicode__(self):
		return self.club.name + " | " + self.heading

class Secy(models.Model):
	club = models.ForeignKey(Club)
	order = models.IntegerField()
	name = models.CharField(max_length=30)
	post = models.CharField(max_length=20)
	email = models.EmailField()
	contact = models.CharField(max_length=20)

	def __unicode__(self):
		return self.club.name + " | " + self.name
