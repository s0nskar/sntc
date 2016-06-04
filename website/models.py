from __future__ import unicode_literals

from django.db import models

class Club(models.Model):
	name = models.CharField(max_length=30)
	about = models.TextField()
	vision = models.TextField()

	def __unicode__(self):
		return self.name

class SubTopic(models.Model):
	club = models.ForeignKey('Club')
	heading = models.CharField(max_length=20)
	about = models.TextField()

	def __unicode__(self):
		return self.club

class Vision(models.Model):
	name = models.CharField(max_length=30)
	post = models.CharField(max_length=30)
	text = models.TextField()

	def __unicode__(self):
		return self.name