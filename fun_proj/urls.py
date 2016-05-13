from __future__ import absolute_import
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from apps.blog.sitemaps import PostSitemap
from apps.blog.views import HomePageView 
admin.autodiscover()

sitemaps = {
          'posts': PostSitemap,
        }

urlpatterns = patterns(
    '',
    # url(r'^$', 'fun_proj.views.home', name='home'),
    #url(r'^$', include('apps.blog.urls', namespace = 'blog')),
    url(r'^$', HomePageView.as_view()),
    url(r'^blog/', include('apps.blog.urls', namespace = 'blog')),
    url(r'^accounts/', include('apps.accounts.urls', namespace = 'accounts')),
    url(r'^blogadmin/', include(admin.site.urls)),
    url(r'^comments/', include('fluent_comments.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name = 'django.contrib.sitemaps.views.sitemap'),
    #url(r'^social-accounts/', include('allauth.urls')),
    #url('', include('social.apps.django_app.urls', namespace = 'social')),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

