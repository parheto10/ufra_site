# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'slug', 'auteur', 'publish', 'status', 'thumb')
    list_filter = ('status', 'created', 'publish', 'auteur')
    search_fields = ('titre', 'message',)
    prepopulated_fields = {'slug': ('titre',)}
    raw_id_fields = ('auteur', )
    date_hierarchy = 'publish'
    ordering = ['status', '-publish']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('nom', 'email', 'body')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

# Register your models here.
