# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-11 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardroom',
            name='max_num',
            field=models.IntegerField(default=10),
        ),
    ]