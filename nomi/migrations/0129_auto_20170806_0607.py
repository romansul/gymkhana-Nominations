# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-06 06:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0128_auto_20170806_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='end_date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
