# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,render_to_response
from django.template import RequestContext

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,render_to_response,redirect
from django.template import RequestContext
from django.contrib import messages


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

	forms=PostForm(request.POST or None)

	if forms.is_valid():
		instance=forms.save(commit=False)
		instance.save()
		#Success Redirect
		messages.success(request,"Post created successfully")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.success(request,"Post not created look something went wrong")	
		
	context={
	"form":forms,
	"title":"Create"
	}

	return render(request,"post_form.html",context)	

	


def post_update(request,id=None):

	instance=get_object_or_404(Post,id=id)

	forms=PostForm(request.POST or None,instance=instance)

	if forms.is_valid():
		instance=forms.save(commit=False)
		print forms.cleaned_data.get("title")
		instance.save()
		#Success Redirect
		messages.success(request,"<a href='#'> Post</a> updated successfully",extra_tags="safe_link")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.success(request,"Post not updated successfully looks something went wrong")	

	context={
		"title":"Post detail",
		"post":instance,
		"form":forms
	}


	return render(request,"post_form.html",context)

def post_delete(request,id=None):
	instance=get_object_or_404(Post,id=id)
	instance.delete()

	messages.success(request,"Post deleted successfully")
	return redirect("posts:list")
	# return HttpResponseRedirect(instance.get_absolute_url())

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

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
