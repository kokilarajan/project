# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-11 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buk', '0004_auto_20180811_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='status',
            field=models.CharField(blank=True, choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=15, null=True),
        ),
    ]
