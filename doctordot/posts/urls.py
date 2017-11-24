
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_index),
    url(r'^create/$', views.post_create),
    url(r'^details/$', views.post_details),
    url(r'^delete/$', views.post_delete),
    url(r'^update/$', views.post_update),
    #url(r'^posts/$', views.post_index),
]