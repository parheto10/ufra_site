# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='contenu',
            field=models.TextField(verbose_name='contenu'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='nom',
            field=models.CharField(max_length=80, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titre',
            field=models.CharField(max_length=250, verbose_name='titre'),
        ),
    ]
