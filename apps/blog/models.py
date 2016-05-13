from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from .markdown import Engine
from django.template import Template, Context
import datetime as dt

class Author(models.Model):
    user = models.OneToOneField( User, on_delete = models.CASCADE, primary_key = True)
    homepage = models.URLField(null = True, blank = True)
    
    def __unicode__(self):
        return self.user.__unicode__()


def upload_location(instance, filename):
    """
    Every file is uploaded into the subfolder "model"
    where "model" is the literal string name of the model where filefield
    is defined there.
    """
    return "%s/%s" %(instance.__class__.__name__, filename)

## We save a rendered html of the user post, right on the spot before
## saving it in db.
markdown = Engine()

class Post(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length = 500, unique = True)
    body = models.TextField(max_length = 10000)
    html = models.TextField(max_length = 10000, blank = True)
    date = models.DateField(default = dt.date.today, editable = True)
    slug = models.SlugField(max_length = 255, blank = True)
    published = models.BooleanField(default= False)
  
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        pre_html = markdown(self.body)
        template = Template(pre_html)
        self.html = template.render(Context({}))
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', kwargs = {'slug': self.slug})

    class Meta:
        ordering = ["-date"]

class Image(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = upload_location, 
            null = True)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length = 20)
    slug = models.SlugField(max_length = 255, blank = True)
    posts = models.ManyToManyField(Post, related_name = 'tags')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tagdetail', kwargs = {'slug': self.slug})

   
