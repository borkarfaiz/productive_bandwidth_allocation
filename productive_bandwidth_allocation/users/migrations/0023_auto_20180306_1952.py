# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 14:22
from __future__ import unicode_literals

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0022_auto_20180223_1548'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usage',
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2018, 3, 6, 14, 22, 40, 421617, tzinfo=utc),
                                   verbose_name='Birth date of user'),
        ),
    ]
