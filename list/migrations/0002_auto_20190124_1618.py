# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-24 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default=b'null', max_length=100),
        ),
        migrations.AlterField(
            model_name='usercategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='list.Category'),
        ),
    ]
