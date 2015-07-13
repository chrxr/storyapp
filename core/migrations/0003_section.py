# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20150711_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('body_content', models.TextField(verbose_name='Story body')),
                ('votes', models.IntegerField(verbose_name='Number of votes', default=0)),
                ('status', models.CharField(max_length=255, choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('submitted', 'Submitted')], verbose_name='Story status', default='submitted')),
                ('story', models.ForeignKey(to='core.story')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Story sections',
                'verbose_name': 'Story section',
            },
        ),
    ]
