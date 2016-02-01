# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160126_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='homepage',
            field=models.URLField(null=True, blank=True),
        ),
    ]
