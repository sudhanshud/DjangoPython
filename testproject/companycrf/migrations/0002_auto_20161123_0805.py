# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companycrf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='cname',
        ),
    ]
