# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=255)),
                ('player_one_name', models.CharField(default='No Player Assigned', max_length=255)),
                ('player_two_name', models.CharField(default='No Player Assigned', max_length=255)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
