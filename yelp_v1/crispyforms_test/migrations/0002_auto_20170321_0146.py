# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-21 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crispyforms_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]