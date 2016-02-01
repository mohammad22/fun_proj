from django.views import generic

from . import models

class HomePageView(generic.ListView):
    model = models.Post
    ordering = '-date'

class PostView(generic.DetailView):

    model = models.Post
    


