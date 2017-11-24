# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .models import Post 


# Create your views here.
def post_index(request):

	queryset=Post.objects.all()

	print queryset

	return render(request,"index.html")


def post_create(request):

	return HttpResponse("post_create")

def post_details(request):

	return HttpResponse("post_details")		


def post_update(request):

	return HttpResponse("post_update")

def post_delete(request):

	return HttpResponse("post_delete")	

