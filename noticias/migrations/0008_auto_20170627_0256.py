# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0007_auto_20170627_0238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admincondominio',
            name='condominio',
        ),
        migrations.RemoveField(
            model_name='copropietario',
            name='condominio',
        ),
        migrations.AddField(
            model_name='admincondominio',
            name='fono',
            field=models.CharField(default=1, max_length=144),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='copropietario',
            name='correo',
            field=models.CharField(default=1, max_length=144),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='copropietario',
            name='fono',
            field=models.CharField(default=1, max_length=144),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Condominio',
        ),
    ]
