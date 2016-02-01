from __future__ import absolute_import
from django.conf.urls import patterns, url, include
from . import views


list_patterns = patterns(

    '',
    url(r'^$', views.HomePageView.as_view(), name = 'postbriefs'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.PostView.as_view(), name = 'post'), 
)

urlpatterns = patterns(
    '',
    url(r'', include(list_patterns)),
)
