# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_section_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='slug',
            field=models.CharField(null=True, blank=True, verbose_name='Story slug', max_length=255),
        ),
    ]
