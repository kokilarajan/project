# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-11 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buk', '0002_auto_20180810_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='catg_type',
            field=models.CharField(choices=[('COMEDY', 'COMEDY'), ('HORROR', 'HORROR'), ('ROMANCE', 'ROMANCE'), ('KIDS', 'KIDS'), ('SCIENCE', 'SCIENCE'), ('LITERATURE', 'LITERATURE'), ('FAIRY TALES', 'FAIRY TALES'), ('MYSTERY', 'MYSTERY'), ('DRAMA', 'DRAMA'), ('COOKING', 'COOKING')], max_length=100),
        ),
        migrations.DeleteModel(
            name='Bookcatg',
        ),
    ]