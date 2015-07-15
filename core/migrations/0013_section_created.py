# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_section_votes_cast'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
    ]
