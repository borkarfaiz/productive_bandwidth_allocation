# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-22 03:41
from __future__ import unicode_literals

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0028_auto_20180422_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='usage',
            name='class_of_user',
            field=models.CharField(default=1, max_length=10, verbose_name='User Class'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2000, 4, 27, 3, 41, 47, 993441, tzinfo=utc),
                                   verbose_name='Birth date of user'),
        ),
    ]
