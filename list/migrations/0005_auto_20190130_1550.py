# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-30 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_auto_20190124_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='list.Category'),
        ),
        migrations.AlterField(
            model_name='usercategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='list.Category'),
        ),
    ]