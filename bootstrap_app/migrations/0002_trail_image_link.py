# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='image_link',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]