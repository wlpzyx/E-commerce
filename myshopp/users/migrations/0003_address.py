# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-22 03:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20190320_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('recv_name', models.CharField(max_length=100, verbose_name='收货人')),
                ('recv_tel', models.CharField(max_length=20, verbose_name='收货人的电话号码')),
                ('province', models.CharField(max_length=100, verbose_name='收货人的省份')),
                ('city', models.CharField(max_length=100, verbose_name='收货人的城市')),
                ('area', models.CharField(max_length=100, verbose_name='收货人的县区')),
                ('street', models.CharField(max_length=255, verbose_name='收货人的街道')),
                ('desc', models.CharField(max_length=255, verbose_name='详细地址')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否是默认地址')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='地址的所属用户')),
            ],
        ),
    ]
