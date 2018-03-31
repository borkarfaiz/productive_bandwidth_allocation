# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-20 17:33
from __future__ import unicode_literals

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0025_auto_20180306_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2000, 3, 25, 17, 33, 14, 483321, tzinfo=utc),
                                   verbose_name='Birth date of user'),
        ),
    ]