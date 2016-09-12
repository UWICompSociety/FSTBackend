# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 11:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0034_auto_20160826_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 29, 11, 53, 43, 96417, tzinfo=utc), editable=False, verbose_name=b'auto_now_add=true'),
        ),
    ]
