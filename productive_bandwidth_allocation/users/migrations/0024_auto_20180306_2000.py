# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 14:30
from __future__ import unicode_literals

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0023_auto_20180306_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2000, 3, 10, 14, 30, 8, 188703, tzinfo=utc),
                                   verbose_name='Birth date of user'),
        ),
    ]
