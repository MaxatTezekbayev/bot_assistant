# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant_telegram', '0003_story_validation_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log_msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=200)),
            ],
        ),
    ]
