# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Param',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Param1', models.FloatField(null=True, blank=True)),
                ('Param2', models.FloatField(null=True, blank=True)),
                ('Param3', models.FloatField(null=True, blank=True)),
                ('Param4', models.FloatField(null=True, blank=True)),
                ('Param5', models.FloatField(null=True, blank=True)),
                ('Param6', models.FloatField(null=True, blank=True)),
                ('Param7', models.FloatField(null=True, blank=True)),
                ('Param8', models.FloatField(null=True, blank=True)),
                ('Param9', models.FloatField(null=True, blank=True)),
                ('Param10', models.FloatField(null=True, blank=True)),
                ('month_num', models.IntegerField()),
                ('company', models.ForeignKey(to='companycrf.Company')),
            ],
        ),
    ]
