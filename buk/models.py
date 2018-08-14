# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Books(models.Model):
	CATEGORY_CHOICES=( ('COMEDY','COMEDY'),
						('HORROR','HORROR'),
						('ROMANCE','ROMANCE'),
						('KIDS','KIDS'),
						('SCIENCE','SCIENCE'),
						('LITERATURE','LITERATURE'),
						('FAIRY TALES','FAIRY TALES'),
						('MYSTERY','MYSTERY'),
						('DRAMA','DRAMA'),
						('COOKING','COOKING')
						)
	STATUS_CHOICES =(('Available', 'Available'),('Unavailable', 'Unavailable'))

	catg_type=models.CharField(max_length=100,choices=CATEGORY_CHOICES,null=True,blank=True)
	buk_by=models.ForeignKey(User,null=True,blank=True)
	buk_cover=models.ImageField(upload_to='sample_img/',null=True,blank=True)
	buk_name=models.CharField(max_length=100,null=True,blank=True)
	buk_author=models.CharField(max_length=200,null=True,blank=True)
	buk_price=models.IntegerField(null=True,blank=True)
	status=models.CharField(max_length=15,choices=STATUS_CHOICES,null=True,blank=True)
	
	created_date=models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.buk_name
