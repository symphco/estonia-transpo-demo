# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-01 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180731_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress')], max_length=30),
        ),
        migrations.AlterField(
            model_name='rideorder',
            name='direction_option',
            field=models.CharField(blank=True, choices=[('Roundtrip', 'Roundtrip'), ('Oneway', 'Oneway')], default='Roundtrip', max_length=30),
        ),
        migrations.AlterField(
            model_name='rideorder',
            name='payment_option',
            field=models.CharField(blank=True, choices=[('Child', 'Child'), ('Subsidised', 'Subsidised'), ('Regular', 'Regular')], default='Child', max_length=30),
        ),
        migrations.AlterField(
            model_name='rideorder',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Directed', 'Directed')], max_length=30),
        ),
    ]
