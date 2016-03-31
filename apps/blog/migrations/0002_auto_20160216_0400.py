# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to=apps.blog.models.upload_location),
        ),
        migrations.AlterField(
            model_name='image',
            name='post',
            field=models.ForeignKey(related_name='Images', to='blog.Post'),
        ),
    ]
