# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 06:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assistant_telegram', '0008_auto_20171026_1210'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Undefined_msg',
        ),
    ]