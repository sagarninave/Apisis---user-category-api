# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-24 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20190124_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
