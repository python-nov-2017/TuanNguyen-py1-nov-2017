# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0002_user_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.CharField(default='admin', max_length=255),
            preserve_default=False,
        ),
    ]