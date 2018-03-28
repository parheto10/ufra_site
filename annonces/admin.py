# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Annonce, Temoignage


class AnnoncesAdmin(admin.ModelAdmin):
    list_display = ["titre", "modifier_le", "ajouter_le"]
    prepopulated_fields = {'slug': ('titre',)}

    class Meta:
        model = Annonce

admin.site.register(Annonce, AnnoncesAdmin)
admin.site.register(Temoignage)

# Register your models here.
