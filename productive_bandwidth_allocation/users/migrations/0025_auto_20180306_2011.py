# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 14:41
from __future__ import unicode_literals

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0024_auto_20180306_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url',
                 models.URLField(help_text='Enter the url of a website you want to visit', verbose_name='site_url')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2000, 3, 10, 14, 41, 42, 71175, tzinfo=utc),
                                   verbose_name='Birth date of user'),
        ),
        migrations.AddField(
            model_name='siteurl',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                    verbose_name='user'),
        ),
    ]