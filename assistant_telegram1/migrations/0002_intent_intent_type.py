# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant_telegram1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='intent',
            name='intent_type',
            field=models.CharField(choices=[('msg', 'message'), ('action', 'action')], default='msg', max_length=10),
        ),
    ]