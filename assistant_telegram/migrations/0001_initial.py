# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 07:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Context_chat',
            fields=[
                ('chat_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('intent', models.CharField(max_length=60)),
                ('validated_action', models.BooleanField()),
                ('prev_msg_from_bot', models.CharField(default=' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('value', models.CharField(max_length=60)),
                ('confidence', models.FloatField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assistant_telegram.Context_chat')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('intent', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('story_type', models.CharField(choices=[('msg', 'message'), ('action', 'action')], default='msg', max_length=10)),
                ('message', models.TextField(default=' ')),
                ('action_name', models.CharField(default=' ', max_length=60)),
                ('answer', models.TextField(default=' ')),
                ('name', models.CharField(default=' ', max_length=60)),
                ('desc', models.CharField(default=' ', max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Story_entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('question', models.CharField(max_length=100)),
                ('intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assistant_telegram.Story')),
            ],
        ),
        migrations.CreateModel(
            name='Undefined_msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=200)),
            ],
        ),
    ]