# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-08 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_second_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='second_name',
        ),
    ]
