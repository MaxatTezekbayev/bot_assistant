# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 05:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assistant_telegram', '0005_auto_20171025_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story_action',
            fields=[
                ('intent', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('validation_option', models.BooleanField(default='False')),
                ('action_name', models.CharField(default=' ', max_length=60)),
                ('action_answer', models.TextField(default=' ')),
                ('transcript', models.CharField(default=' ', max_length=60)),
                ('desc', models.TextField(default=' ')),
            ],
        ),
        migrations.CreateModel(
            name='Story_msg',
            fields=[
                ('intent', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('msg_example', models.TextField(default=' ')),
                ('anwer', models.TextField(default=' ')),
            ],
        ),
        migrations.RenameModel(
            old_name='Log_msg',
            new_name='Log',
        ),
        migrations.AlterField(
            model_name='story_entity',
            name='intent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assistant_telegram.Story_action'),
        ),
        migrations.DeleteModel(
            name='Story',
        ),
    ]