from __future__ import absolute_import
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe

from .models import Author, Post, Image, Tag

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class TagInline(admin.TabularInline):
    model = Tag.posts.through
    extra = 1

class PostAdmin(admin.ModelAdmin):
    exclude = ('slug', 'html')
    inlines = [ImageInline, TagInline]
    #readonly_fields = ['date']
    fieldsets = (
        ('Metadata of Post', {
            'fields': ('author', 'title', 'date', 'published'),
            'classes': ('collapse',)
        }),
        ('Post', {
            'fields': ('date', 'body') 
        }),
    ) 
    
    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.title) 
        mark_safe(obj.body)
        mark_safe(obj.html)
        obj.save()

class TagAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)

