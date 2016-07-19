# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 09:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0009_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=400)),
                ('detail', models.TextField()),
                ('image_url', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=datetime.datetime(2016, 7, 19, 9, 59, 32, 42571), editable=False, verbose_name=b'auto_now_add=true')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 19, 9, 59, 32, 12635), editable=False, verbose_name=b'auto_now_add=true'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 19, 9, 59, 32, 27624), editable=False, verbose_name=b'auto_now_add=true'),
        ),
    ]
