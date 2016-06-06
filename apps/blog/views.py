from django.views import generic
from django.shortcuts import render_to_response
from . import models
from django.http import JsonResponse
from django.views.decorators.cache import cache_page

class cacheMixin(object):
    cache_timeout =  60 * 60 * 24  

    def get_cache_timeout(self):
        return self.cache_timeout
       
    def dispatch(self, *args, **kwargs):
        dis = super(cacheMixin, self).dispatch
        if self.request.user.is_staff:
            return dis(*args, **kwargs)
        else:
            return cache_page(self.get_cache_timeout())(dis)(*args, **kwargs)


@cache_page(60 * 60 * 24)
def about(request):
    return render_to_response('blog/about.html')

class HomePageView(cacheMixin, generic.ListView):
    model = models.Post
    ordering = '-date'
    paginate_by = 3
    def get_queryset(self, *args, **kwargs):
        li = super(HomePageView, self).get_queryset(*args, **kwargs)
        #li.prefetch_related('tags')
        if self.request.user.is_staff:
            return li
        else:
            return li.filter(published=True)

class PostView(cacheMixin, generic.DetailView):
    model = models.Post
    def get_object(self, *args, **kwargs):
        obj = super(PostView, self).get_object(*args, **kwargs)
        obj.images = models.Image.objects.filter(post = obj)
        return obj

@cache_page(60 * 60 * 24)
def TagsView(request):
    tags = models.Tag.objects.all()
    pre_tags = {}
    for t in tags: pre_tags[t.name] = t.get_absolute_url()
    return JsonResponse(pre_tags, safe = False)


class TagDetailView(cacheMixin, generic.DetailView):
    model = models.Tag
    def get_object(self, *args, **kwargs):
        obj = super(TagDetailView, self).get_object(*args, **kwargs)
        posts = models.Post.objects.filter(tags__name__contains=obj.name)
        if self.request.user.is_staff:
            return posts
        else:
            return posts.filter(published=True)


