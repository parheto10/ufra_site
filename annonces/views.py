# -*- coding: utf-8 -*-
from __future__ import unicode_literals


try:
    from urllib import quote_plus
except:
    pass

from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import ContactForm, TForm
from .models import Annonce, Temoignage

def temoigne(request):
    t_form = TForm(request.POST or None, request.FILES or None)
    if t_form.is_valid():
        instance = t_form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Temoignage ajouter avec success")
        return redirect('annonces:index')
    context = {
        "t_form": t_form,
    }
    return render(request, "annonces/index.html", context)

def index(request):
    today = timezone.now().date()
    annonces = Annonce.objects.active()  # .order_by("-timestamp")

    context = {
        "annonces": annonces,
        "titre": "Ufra-Annonces",
        #"page_request_var": page_request_var,
        "today": today,
    }
    return render(request, 'annonces/index.html', context)

def temoignage(request):
    form = TForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Temoignage ajoute avec success, Merci !!")
        return redirect('annonces:temoignage')

    today = timezone.now().date()
    queryset_list = Temoignage.objects.all().order_by("-cree_le")
    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "form": form,
        "object_list": queryset,
        "titre": "Temoignages",
        "page_request_var": page_request_var,
        "today": today,
    }
    return render(request, "annonces/temoignages.html", context)

def annonces(request):
    today = timezone.now().date()
    queryset_list = Annonce.objects.active()  # .order_by("-timestamp")

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(titre__icontains=query) |
            Q(detail__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 8)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "titre": "Ufra-Annonces",
        "page_request_var": page_request_var,
        "today": today,
    }
    return render(request, "annonces/annonces.html", context)

def about(request):
    today = timezone.now().date()
    queryset_list = Annonce.objects.active()  # .order_by("-timestamp")
    paginator = Paginator(queryset_list, 3)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "titre": "Ufra-Annonces",
        "page_request_var": page_request_var,
        "today": today,
    }
    return render(request, 'annonces/about.html', context)


def contact(request):
    #today = timezone.now().date()
    queryset_list = Annonce.objects.active()  # .order_by("-timestamp")
    paginator = Paginator(queryset_list, 3)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    titre = 'Formulaire de Contact'
    titre_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        from_email = form.cleaned_data.get("email")
        from_message = form.cleaned_data.get("message")
        from_telephone = form.cleaned_data.get("telephone")
        from_nom = form.cleaned_data.get("nom")
        sujet = 'Formulaire de Contact'
        to_email = ['settings.EMAIL_HOST_USER']
        contact_message = "Message : %s\n\n Nom et Prenoms : %s\n\n Conatct : %s\n\n de : %s" % (
            from_message,
            from_nom,
            from_telephone,
            from_email
            )
        send_mail(
            sujet,
            contact_message,
            from_email,
            to_email,
            fail_silently=True,
        )
        messages.success(request, "Mail Envoyer Avec Success")
        return redirect("annonces:contact")
    else:
        context = {
            "form": form,
            "titre": titre,
            "titre_align_center": titre_align_center,
            "object_list": queryset,
            "annonces": "Ufra-Annonces",
            "page_request_var": page_request_var,
        }
        return render(request, "annonces/contact.html", context)

# Create your views here.
