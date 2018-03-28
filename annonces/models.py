# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os,time,csv,pdb
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from sorl.thumbnail import ImageField,get_thumbnail
from django.utils.text import slugify
from django.db.models.signals import pre_save

from django.utils.translation import gettext_lazy as _

class AnnonceManager(models.Manager):
    def active(self):
        return super(AnnonceManager, self).get_queryset().filter(active=True).filter(ajouter_le__lte=timezone.now())

class Annonce(models.Model):
    titre = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    modifier_le = models.DateTimeField(auto_now=True, auto_now_add=False)
    ajouter_le = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    detail = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    object = models.Manager()  # the default Manager
    objects = AnnonceManager()  # Post activer

    class Meta:
        ordering = ('-ajouter_le', '-modifier_le')

    def __str__(self):
        return self.titre.encode('utf-8').strip()

    def get_absolute_url(self):
        return reverse('annonces:annonce_detail',
                       args=[self.ajouter_le.year,
                             self.ajouter_le.strftime('%m'),
                             self.ajouter_le.strftime('%d'),
                             self.slug])

    def save(self, force_insert=False, force_update=False):
        self.titre = self.titre.upper()
        super(Annonce, self).save(force_insert, force_update)

    def thumb(self):
        if self.image:
            thumb = get_thumbnail(self.image, "120x100", crop='center', quality=99)
            return "<image src='%s' />" % thumb.url
        else:
            return "Aucun Image"

    thumb.short_description = ('image')
    thumb.allow_tags = True

    def contenu(self):
        if len(self.detail) > 50:
            return self.detail[0:49] + "  ..."
        else:
            return self.detail

def create_slug(instance, new_slug=None):
    slug = slugify(instance.titre)
    if new_slug is not None:
        slug = new_slug
    qs = Annonce.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Annonce)



class Temoignage(models.Model):
    nom = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    texte = models.TextField()
    image = models.ImageField(upload_to='temoignages/%Y/%m/%d', null=True, blank=True)
    cree_le = models.DateTimeField(auto_now_add=True)
    modifie_le = models.DateTimeField(auto_now=True)

    def contenu(self):
        if len(self.texte) > 50:
            return self.texte[0:49] + "  ..."
        else:
            return self.texte

    def __str__(self):
        return 'temoignage {} de {}'.format(self.nom, self.texte).encode('utf-8').strip()

    class Meta:
        ordering = ('-cree_le', )





# Create your models here.
