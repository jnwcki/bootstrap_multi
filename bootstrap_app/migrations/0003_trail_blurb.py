# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap_app', '0002_trail_image_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='blurb',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]