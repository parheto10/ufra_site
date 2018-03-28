# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps.config import MODELS_MODULE_NAME
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from sorl.thumbnail import ImageField,get_thumbnail

from django.utils.translation import gettext_lazy as _

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
     STATUS_CHOICES = (
         ('draft', 'En Attente'),
         ('published', 'Publier'),
     )
     titre = models.CharField( max_length=250)
     slug = models.SlugField(max_length=250, unique_for_date='publish')
     auteur = models.ForeignKey(User, related_name='blog_posts')
     message = models.TextField()
     publish = models.DateTimeField(default=timezone.now)
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)
     image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

     object = models.Manager() #the default Manager
     publier = PublishedManager() # Post Publier
     tags = TaggableManager()

     class Meta:
        ordering = ('-publish',)

     def __str__(self):
        return self.titre.encode('utf-8').strip()

     def get_absolute_url(self):
         return reverse('posts:post_detail',
                        args=[self.publish.year,
                              self.publish.strftime('%m'),
                              self.publish.strftime('%d'),
                              self.slug])

     def thumb(self):
         if self.image:
             thumb = get_thumbnail(self.image, "120x100", crop='center', quality=99)
             return "<image src='%s' />" % thumb.url
         else:
             return "Aucun"

     thumb.short_description = ('image')
     thumb.allow_tags = True


class Comment(models.Model):
     post = models.ForeignKey(Post, related_name='comments')
     nom = models.CharField(max_length=80)
     email = models.EmailField()
     contenu = models.TextField()
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)
     active = models.BooleanField(default=True)
     class Meta:
        ordering = ('created',)
     def __str__(self):
        return 'Commentaire de {} sur {}'.format(self.nom, self.post).encode('utf-8').strip()

# Create your models here.
