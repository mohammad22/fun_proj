from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'fun_proj.views.home', name='home'),
    url(r'^blog/', include('apps.blog.urls', namespace = 'blog')),
    url(r'^accounts/', include('apps.accounts.urls', namespace = 'accounts')),
    url(r'^admin/', include(admin.site.urls)),
]
