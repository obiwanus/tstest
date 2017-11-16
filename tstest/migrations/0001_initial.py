# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_endpoint', models.CharField(max_length=255)),
                ('http_method', models.CharField(default='', max_length=10)),
                ('response_ms', models.IntegerField(default=0)),
                ('status_code', models.IntegerField(default=200)),
                ('received', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]