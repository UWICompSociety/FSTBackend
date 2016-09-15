# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 15:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0051_auto_20160915_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 15, 28, 20, 306848, tzinfo=utc), editable=False, verbose_name=b'auto_now_add=true'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 15, 28, 20, 299258, tzinfo=utc), editable=False, verbose_name=b'auto_now_add=true'),
        ),
    ]
