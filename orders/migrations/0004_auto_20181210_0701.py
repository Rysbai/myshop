# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-10 07:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20181210_0527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='addres',
            new_name='address',
        ),
    ]