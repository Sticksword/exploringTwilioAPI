# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_sid', models.CharField(max_length=34)),
                ('time_called', models.DateTimeField(auto_now_add=True)),
                ('time_delay', models.IntegerField(blank=True, null=True)),
                ('to_number', models.CharField(max_length=15)),
                ('from_number', models.CharField(blank=True, max_length=15, null=True)),
                ('digits_entered', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
