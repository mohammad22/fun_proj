from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

# Create your models here

class Author(models.Model):
    user = models.OneToOneField(
            User,
            on_delete = models.CASCADE,
            primary_key = True)
    homepage = models.URLField(null = True, blank = True)

    def __unicode__(self):
        return self.user.__unicode__()

class Post(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length = 500, unique = True)
    body = models.TextField(max_length = 10000)
    date = models.DateField()
    slug = models.SlugField(max_length = 255, blank = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', kwargs = {'slug': self.slug})


