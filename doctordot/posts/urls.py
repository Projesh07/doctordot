
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_index,name="list"),
    url(r'^create/$', views.post_create),
    url(r'^(?P<id>\d+)/$', views.post_details, name="detail"),

    url(r'^delete/$', views.post_delete),
    url(r'^update/$', views.post_update),

    url(r'^(?P<id>\d+)/delete/$', views.post_delete),
    url(r'^(?P<id>\d+)/edit/$', views.post_update,name="update"),

    #url(r'^posts/$', views.post_index),
]