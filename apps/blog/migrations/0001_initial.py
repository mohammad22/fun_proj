# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import apps.blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('homepage', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to=apps.blog.models.upload_location, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=500)),
                ('body', models.TextField(max_length=10000)),
                ('html', models.TextField(max_length=10000, blank=True)),
                ('date', models.DateField(auto_now=True)),
                ('slug', models.SlugField(max_length=255, blank=True)),
                ('published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to='blog.Author')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(related_name='Images', blank=True, to='blog.Post'),
        ),
    ]
