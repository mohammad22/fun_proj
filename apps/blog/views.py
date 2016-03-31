from django.views import generic
from django.shortcuts import render_to_response
from . import models

def about(request):
    return render_to_response('blog/about.html')

class HomePageView(generic.ListView):
    model = models.Post
    ordering = '-date'
    paginate_by = 5
    def get_queryset(self, *args, **kwargs):
        list = super(HomePageView, self).get_queryset(*args, **kwargs)
        if self.request.user.is_staff:
            return list
        else:
            return list.filter(published=True)

class PostView(generic.DetailView):
    model = models.Post
    def get_object(self, *args, **kwargs):
        obj = super(PostView, self).get_object(*args, **kwargs)
        obj.images = models.Image.objects.filter(post = obj)
        return obj

class TagsView(generic.ListView):
    model = models.Tag

class TagDetailView(generic.DetailView):
    model = models.Tag
    def get_object(self, *args, **kwargs):
        obj = super(TagDetailView, self).get_object(*args, **kwargs)
        posts = models.Post.objects.filter(tags__name__contains=obj.name)
        return posts


