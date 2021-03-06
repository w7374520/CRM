# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-03 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0006_remove_permission_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='pid',
            field=models.ForeignKey(blank=True, help_text='对于无法作为菜单的URL，可以为其选择一个可以作为菜单的权限，那么访问时，则默认选中此权限', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ps', to='rbac.Permission', verbose_name='默认选中权限'),
        ),
    ]
