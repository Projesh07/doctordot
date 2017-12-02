# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.




class Post(models.Model):

	
	def upload_location(self,filename):
		return "post_image/%s/%s" % (self.id,filename)	

	title=models.CharField(max_length=120)
	image=models.ImageField(null=True,blank=True,height_field="height_field",width_field="width_field",upload_to=upload_location)
	height_field=models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	content=models.TextField()
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	created=models.DateTimeField(auto_now=False,auto_now_add=True)
	

	def __unicode__ (self):

		return self.title
	def __str__(self):
		return self.title


	def get_absolute_url(self):

		return reverse("posts:detail",kwargs={"id":self.id})
		#return "/posts/%s/"%(self.id)	

	class Meta:
		ordering=["-created","-updated"]	

