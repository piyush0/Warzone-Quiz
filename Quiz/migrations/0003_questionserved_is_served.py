# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-08 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_questionserved'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionserved',
            name='is_served',
            field=models.BooleanField(default=False),
        ),
    ]