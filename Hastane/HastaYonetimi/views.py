from django.db import connection
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
#from .models import Patient
from .models import Patient
import logging


def Hasta(request):
    return render(request , 'Hastane/HastaEkrani.html')




logger = logging.getLogger(__name__)

def hasta_olustur(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        dogum_tarihi = request.POST.get('dogum_tarihi')
        cinsiyet = request.POST.get('cinsiyet')

        # Basit doğrulama
        if ad and soyad and dogum_tarihi and cinsiyet:
            try:
                new_patient = Patient.objects.create(
                    patient_name=ad,
                    patient_last_name=soyad,
                    p_birth_date=dogum_tarihi,
                    p_gender=cinsiyet,
                    phone_number='N/A',
                    p_address='N/A'
                )
                return render(request, 'Hastane/hasta_olustur.html', {'success': True})
            except Exception as e:
                logger.error(f"Hasta kaydı sırasında bir hata oluştu: {e}")
                error_message = "Hasta kaydı sırasında bir hata oluştu."
                return render(request, 'Hastane/hasta_olustur.html', {'error_message': error_message})
        else:
            error_message = "Lütfen tüm alanları doldurun."
            return render(request, 'Hastane/hasta_olustur.html', {'error_message': error_message})

    return render(request, 'Hastane/hasta_olustur.html')

 

def RandevuIslemleri(request):
    return render(request, 'Hastane/RandevuIslemleri.html') 

def Hasta_listesi(request):
    hasta_listesi = Patient.objects.all()
    context = {
        'hasta_listesi': hasta_listesi
    }
    return render(request, 'Hastane/hasta_listesi.html', context)

def HastaLogin(request):
    return render(request , 'Hastane/HastaLogin.html')

def BilgiGuncelle(request):
    return render(request , 'Hastane/BilgiGuncelle.html')

def RandevuSil(request):
    return render(request , 'Hastane/RandevuSil.html')



