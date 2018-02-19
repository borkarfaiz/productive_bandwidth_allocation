# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-19 10:46
from __future__ import unicode_literals

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0014_auto_20180219_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2018, 2, 19, 10, 46, 7, 308904, tzinfo=utc),
                                   verbose_name='Birth date of user'),
        ),
    ]
