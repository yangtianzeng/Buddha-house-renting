# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-09 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemodel',
            name='price',
            field=models.IntegerField(),
        ),
    ]
