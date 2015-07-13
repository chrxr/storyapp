# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150711_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='postition',
            field=models.IntegerField(verbose_name='Position of section in the story', null=True, blank=True),
        ),
    ]
