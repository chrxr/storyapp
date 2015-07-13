# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_section_postition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='postition',
            new_name='position',
        ),
    ]
