from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	email = models.CharField(max_length=250)
	password = models.CharField(max_length=250)