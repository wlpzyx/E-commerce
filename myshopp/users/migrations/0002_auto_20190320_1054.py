# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-20 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='header',
            field=models.ImageField(default='static/images/head/default.jpg', upload_to='static/images/head', verbose_name='用户头像'),
        ),
    ]
