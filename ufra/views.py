# Error Pages
from django.shortcuts import render

def erreur_500(request):
    return render(request, 'errors/500.html')

def erreur_404(request):
    return render(request, 'errors/404.html')

def erreur_403(request):
    return render(request, 'errors/403.html')

def erreur_400(request):
    return render(request, 'errors/400.html')