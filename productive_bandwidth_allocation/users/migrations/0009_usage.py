# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-12 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0008_auto_20180212_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(default='f', max_length=10)),
                ('education', models.IntegerField()),
                ('related_education', models.IntegerField()),
                ('other', models.IntegerField()),
            ],
        ),
    ]
