from __future__ import absolute_import
from django.contrib import admin
from django.template.defaultfilters import slugify

from .models import Author, Post

class PostAdmin(admin.ModelAdmin):
    exclude = ('slug', )
    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.title) 
        obj.save()

admin.site.register(Author)
admin.site.register(Post)


# Register your models here.
