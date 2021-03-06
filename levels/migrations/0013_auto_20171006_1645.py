# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0012_level_required_attempts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='required_attempts',
            field=models.PositiveIntegerField(default=0, help_text='Users need to try at least this many times before we accept an answer'),
        ),
    ]
