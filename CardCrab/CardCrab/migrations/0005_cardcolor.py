# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-15 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardCrab', '0004_auto_20170315_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]