from __future__ import absolute_import
from django.conf.urls import patterns, url, include
from .views import SignUpView, LoginView, LogoutView

from django.contrib import admin
admin.autodiscover()


list_patterns = patterns(
    '',
    #url(r'^$', views.Accounts.as_view(), name = 'accountList'),
    url(r'^register/', SignUpView.as_view(), name = 'signup'),
    url(r'^login/', LoginView.as_view(), name = 'login'),
    url(r'^logout/', LogoutView.as_view(), name = 'logout'),
)

urlpatterns = patterns(
    '',
    url(r'', include(list_patterns)),
)
