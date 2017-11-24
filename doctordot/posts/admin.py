# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display=("title","content","created","updated")
	list_filter=("title",)
	list_links=("updated",)
	# list_editable=['title']

	search_fields=['title','content']
	class Meta:
		  model=Post

admin.site.register(Post,PostModelAdmin)

# Register your models here.
