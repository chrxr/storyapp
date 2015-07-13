# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Genre')),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='genre',
            field=models.ForeignKey(to='core.Genre', blank=True, null=True),
        ),
    ]
