# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0006_auto_20160522_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='points',
            field=models.IntegerField(default=1),
        ),
    ]