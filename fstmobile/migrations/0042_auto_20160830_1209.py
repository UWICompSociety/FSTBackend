# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 12:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0041_auto_20160830_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 30, 12, 9, 58, 568618, tzinfo=utc), editable=False, verbose_name=b'auto_now_add=true'),
        ),
    ]
