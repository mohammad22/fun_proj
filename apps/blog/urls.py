from __future__ import absolute_import
from django.conf.urls import patterns, url, include
from . import views
from .feeds import LatestPostsFeed


list_patterns = patterns(

    '',
    url(r'^$', views.HomePageView.as_view(), name = 'postbriefs'),
    url(r'^page(?P<page>[0-9]+)/$', views.HomePageView.as_view(), name = 'postbriefs'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.PostView.as_view(), name = 'post'), 
    url(r'^tags/', views.TagsView.as_view(), name = 'tags'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.TagDetailView.as_view(), name = 'tagdetail'),
    #url(r'^archive/$', views.PostArchiveView.as_view(), name = "post_archive"),
    url(r'^about/$', views.about, name = "about"),
    url(r'^feed/$', LatestPostsFeed(), name = 'post_feed'),
)

urlpatterns = patterns(
    '',
    url(r'', include(list_patterns)),
)
