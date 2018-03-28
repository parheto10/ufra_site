# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='ajouter_le',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ajouter_le'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='detail',
            field=models.TextField(blank=True, verbose_name='titre'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='modifier_le',
            field=models.DateTimeField(auto_now=True, verbose_name='modifier_le'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='titre',
            field=models.CharField(max_length=120, verbose_name='titre'),
        ),
        migrations.AlterField(
            model_name='temoignage',
            name='cree_le',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cree_le'),
        ),
        migrations.AlterField(
            model_name='temoignage',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='temoignage',
            name='modifie_le',
            field=models.DateTimeField(auto_now=True, verbose_name='modifie_le'),
        ),
        migrations.AlterField(
            model_name='temoignage',
            name='nom',
            field=models.CharField(max_length=80, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='temoignage',
            name='texte',
            field=models.TextField(verbose_name='texte'),
        ),
    ]
