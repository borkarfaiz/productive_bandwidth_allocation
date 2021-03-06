# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-22 06:52
from __future__ import unicode_literals

import datetime

import django.db.models.deletion
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0035_auto_20180422_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usage',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.UserGroup',
                                       verbose_name='group of user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2000, 4, 27, 6, 52, 3, 936174, tzinfo=utc),
                                   verbose_name='Birth date of user'),
        ),
    ]
