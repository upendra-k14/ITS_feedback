# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-19 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20170219_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestfeedback',
            name='end_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='requestfeedback',
            name='start_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
