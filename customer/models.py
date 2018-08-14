# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
	usr_data  = models.OneToOneField(User)
	profile_pic=models.ImageField(upload_to='media/sample_img/')
	address = models.CharField(max_length=100)
	
	place = models.CharField(max_length=100)
	Phone =models.CharField(max_length=15)

	def __str__(self):
		return self.place
