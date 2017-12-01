# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,render_to_response
from django.template import RequestContext

from .models import Post 
from .forms import PostForm 

# Create your views here.
def post_index(request):

	queryset=Post.objects.all()

	context={
		"posts":queryset,
		"title":"Post list"
	}

	return render(request,"index.html",context)

def post_details(request,id=None):

	instance=get_object_or_404(Post,id=id)
	context={
		"title":"Post detail",
		"post":instance
	}

	return render(request,"post_details.html",context)	


def post_create(request):

	forms=PostForm(request.Post or None)

	if forms.is_valid():
		instance=forms.save(commit=False)
		instance.save()
		
	context={
	"form":forms,
	"title":"Create"
	}

	return render(request,"post_create.html",context)	

	


def post_update(request):

	return HttpResponse("post_update")

def post_delete(request):

	return HttpResponse("post_delete")	

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
