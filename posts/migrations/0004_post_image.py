# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
