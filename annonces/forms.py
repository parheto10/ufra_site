# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Temoignage

class TForm(forms.ModelForm):
    texte = forms.CharField(label=_('Temoignage'), widget=forms.Textarea)
    class Meta:
        model = Temoignage
        fields = [
            'nom',
            'texte',
            'image',
        ]

class ContactForm(forms.Form):
    nom = forms.CharField(label=_('Nom et Prenoms'))
    telephone = forms.CharField(label=_('Contacts'))
    email = forms.EmailField()
    message = forms.CharField(label=_('message'), widget=forms.Textarea)