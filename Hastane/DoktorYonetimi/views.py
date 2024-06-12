from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Doctor  # Doktor modelinizi buraya import edin
from django.contrib.auth import login
from django.contrib.auth.models import User

def DoktorEkrani(request):
    return render(request, "Hastane/DoktorEkrani.html")



def AnaEkran(request):
    return render(request , "Hastane/GirisEkrani.html")



def HastaEkran(request):
    return render(request , "Hastane/HastaEkran.html")



def LoginDoktor(request):
    if request.method == 'POST':
        kullanici_adi = request.POST.get("username")
        sifre = request.POST.get("password")
        
        try:
            # Doktoru veritabanında bul
            doktor = Doctor.objects.get(doctor_name=kullanici_adi, doctor_last_name=sifre)
            
            # Eğer doktor varsa, ona ait bir kullanıcı oluştur veya getir
            user, created = User.objects.get_or_create(username=f"{kullanici_adi}_{sifre}")
            
            # Kullanıcıyı giriş yapmış olarak ayarla
            login(request, user)
            
            return redirect("doktorekrani")
        except Doctor.DoesNotExist:
            return render(request, 'Hastane/LoginDoktor.html', {
                "error": "Kullanici adi veya Sifre yanlis"
            })
    
    return render(request, 'Hastane/LoginDoktor.html')

def HastaLogin(request):
    return render(request , "Hastane/HastaLogin.html")

