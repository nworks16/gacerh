# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-25 16:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ncf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasto',
            name='comprador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detalleg',
            name='itbis',
            field=models.DecimalField(decimal_places=2, max_digits=999999),
        ),
        migrations.AlterField(
            model_name='detalleg',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=999999),
        ),
        migrations.AlterField(
            model_name='detalleg',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=999999),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='total_final',
            field=models.DecimalField(decimal_places=2, max_digits=999999),
        ),
    ]