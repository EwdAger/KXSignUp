# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SignUp', '0002_auto_20170807_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signmessage',
            name='phone_num',
            field=models.CharField(max_length=200, null=True, verbose_name='\u7535\u8bdd'),
        ),
    ]
