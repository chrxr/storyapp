# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0011_auto_20150712_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='votes_cast',
            field=models.ManyToManyField(blank=True, related_name='votes_cast', to=settings.AUTH_USER_MODEL),
        ),
    ]
