# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-29 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180729_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('supervisor', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
