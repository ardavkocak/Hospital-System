from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Patient
from django.contrib import messages
from django.contrib.auth import  login 
from django.contrib.auth.models import User
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
        telefon = request.POST.get('telefon')
        adres = request.POST.get('adres')

        # Basit doğrulama
        if ad and soyad and dogum_tarihi and cinsiyet and telefon and adres:
            try:
                new_patient = Patient.objects.create(
                    patient_name=ad,
                    patient_last_name=soyad,
                    p_birth_date=dogum_tarihi,
                    p_gender=cinsiyet,
                    phone_number=telefon,
                    p_address=adres
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

def hasta_sil(request):
    if request.method == 'POST':
        # Formdan gelen hasta id'sini al
        hasta_id = request.POST.get('hasta_id')
        
        # Hasta objesini sil
        try:
            hasta = Patient.objects.get(pk=hasta_id)
            hasta.delete()
            return redirect('hastacikart')  # Silme işlemi başarılıysa sayfayı yenile
        except Patient.DoesNotExist:
            error_message = "Seçilen hasta bulunamadı."
            return render(request, 'Hastane/Hastacikart.html', {'error_message': error_message})

    # GET isteği durumunda, tüm hastaları listele
    hastalar = Patient.objects.all()

    return render(request, 'Hastane/Hastacikart.html', {'hastalar': hastalar})
 





def Hasta_listesi(request):
    hasta_listesi = Patient.objects.all()
    context = {
        'hasta_listesi': hasta_listesi
    }
    return render(request, 'Hastane/hasta_listesi.html', context)

def HastaLogin(request):
    if request.method == 'POST':
        ad = request.POST.get("firstname")
        soyad = request.POST.get("lastname")
        
        try:
            # Hastayı veritabanında bul
            hasta = Patient.objects.get(patient_name=ad, patient_last_name=soyad)
            
            # Eğer hasta varsa, ona ait bir kullanıcı oluştur veya getir
            user, created = User.objects.get_or_create(username=f"{ad}_{soyad}")
            
            # Kullanıcıyı giriş yapmış olarak ayarla
            login(request, user)
            
            return redirect("hasta")
        except Patient.DoesNotExist:
            return render(request, 'Hastane/HastaLogin.html', {
                "error": "Adiniz veya Soyadiniz yanlis"
            })
    
    return render(request, 'Hastane/HastaLogin.html')

def BilgiGuncelle(request, patient_id):
    
    patient = get_object_or_404(Patient, patient_id=patient_id)
    
    if request.method == 'POST':
        ad = request.POST.get('firstname')
        soyad = request.POST.get('lastname')
        dogum_tarihi = request.POST.get('birth_date')
        cinsiyet = request.POST.get('gender')
        telefon = request.POST.get('phone')
        adres = request.POST.get('address')

        # Basit doğrulama
        if ad and soyad and dogum_tarihi and cinsiyet and telefon and adres:
            try:
                patient.patient_name = ad
                patient.patient_last_name = soyad
                patient.p_birth_date = dogum_tarihi
                patient.p_gender = cinsiyet
                patient.phone_number = telefon
                patient.p_address = adres
                patient.save()

                messages.success(request, "Hasta bilgileri başarıyla güncellendi.")
                return render(request, 'Hastane/BilgiGuncelle.html', {'patient': patient, 'success': "Hasta bilgileri başarıyla güncellendi."})
            except Exception as e:
                logger.error(f"Hasta bilgileri güncelleme sırasında bir hata oluştu: {e}")
                return render(request, 'Hastane/BilgiGuncelle.html', {'patient': patient, 'error': "Hasta bilgileri güncelleme sırasında bir hata oluştu."})
        else:
            return render(request, 'Hastane/BilgiGuncelle.html', {'patient': patient, 'error': "Lütfen tüm alanları doldurun."})

    return render(request, 'Hastane/BilgiGuncelle.html', {'patient': patient})
    





