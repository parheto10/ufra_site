# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			cd  = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect("annonces:index",)
					#return HttpResponse('Authentication Réussit Bienvenus')
				else:
					return HttpResponse('Compte Desactive')
			else:
				return HttpResponse('Parametres de Compte Invalid, Verifie SVP !!')
	else:
		form = LoginForm()
	context = {
		'form': form,
	}
	return render(request, 'compte/login.html', context)

@login_required
def dashboard(request):
	context = {
		'section':'dashboard'
	}
	return render(request, 'compte/dashboard.html', context)

# Create your views here.
