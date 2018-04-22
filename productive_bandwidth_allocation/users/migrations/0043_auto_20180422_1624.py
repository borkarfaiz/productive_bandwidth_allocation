# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-22 10:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_auto_20180422_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2000, 4, 27, 10, 54, 50, 67250, tzinfo=utc), verbose_name='Birth date of user'),
        ),
    ]
