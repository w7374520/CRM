# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-03 12:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0005_menu_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='icon',
        ),
    ]
