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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_index(request):

	queryset_list=Post.objects.all() #.order_by("-created")
	paginator = Paginator(queryset_list, 2) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)

	context={
		"posts":queryset,
		"title":"Post list"
	}

	return render(request,"index.html",context)

def post_details(request,slug=None):


	instance=get_object_or_404(Post,slug=slug)
	context={
		"title":"Post detail",
		"post":instance
	}

	return render(request,"post_details.html",context)	


def post_create(request):


	forms=PostForm(request.POST or None, request.FILES or None)

	if forms.is_valid():
		instance=forms.save(commit=False)
		instance.save()
		#Success Redirect
		messages.success(request,"Post created successfully")
		return HttpResponseRedirect(instance.get_absolute_url())
	# else:
	# 	messages.error(request,"Post not created look something went wrong")	
		
	context={
	"form":forms,
	"title":"Create"
	}

	return render(request,"post_form.html",context)	

	


def post_update(request,slug=None):

	instance=get_object_or_404(Post,slug=slug)

	forms=PostForm(request.POST or None,request.FILES or None,instance=instance)

	if forms.is_valid():
		instance=forms.save(commit=False)
		print forms.cleaned_data.get("title")
		instance.save()
		#Success Redirect
		messages.success(request,"<a href='#'> Post</a> updated successfully",extra_tags="safe_link")
		return HttpResponseRedirect(instance.get_absolute_url())
	# else:
	# 	messages.error(request,"Post not updated successfully looks something went wrong")	

	context={
		"title":"Post detail",
		"post":instance,
		"form":forms
	}


	return render(request,"post_form.html",context)

def post_delete(request,slug=None):
	instance=get_object_or_404(Post,slug=slug)
	instance.delete()

	messages.success(request,"Post deleted successfully")
	return redirect("posts:list")
	# return HttpResponseRedirect(instance.get_absolute_url())



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
