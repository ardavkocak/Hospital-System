from django.db import connection
from django.shortcuts import render

# Create your views here.

def AdminEkrani(request):
    return render(request , "Hastane/AdminEkrani.html")

def AdminYonetimEkrani(request):
    return render(request , "Hastane/AdminYonetimEkrani.html")

def DoktorEkle(request):
    
    return render(request , "Hastane/DoktorEkle.html")

def DoktorSil(request):
    return render(request , "Hastane/DoktorSil.html")

def DoktorGoruntule(request):
    return render(request , "Hastane/DoktorGoruntule.html")

def HastaSil(request):
    return render(request , "Hastane/HastaSil.html")

