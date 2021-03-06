# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-19 20:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20170316_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testadmin',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='answer_file',
            field=models.FileField(blank=True, max_length=200, upload_to=b'/Users/akshat/Documents/Tand_Labs/automated_testing/media/Testuser', verbose_name='File'),
        ),
    ]
