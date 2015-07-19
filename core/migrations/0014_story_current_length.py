# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_section_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='current_length',
            field=models.IntegerField(null=True, blank=True, default=0),
        ),
    ]
