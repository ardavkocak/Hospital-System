from django.db import connection
from django.shortcuts import render
from DoktorYonetimi.models import Doctor
from django.shortcuts import render, redirect
import logging
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Admin

# Create your views here.

def AdminEkrani(request):
    if request.method == 'POST':
        kullanici_adi = request.POST.get("username")
        soyad = request.POST.get("soyad")
        
        try:
            # Admini veritabanında bul
            admin = Admin.objects.get(admin_name=kullanici_adi, admin_last_name=soyad)
            
            # Eğer admin varsa, ona ait bir kullanıcı oluştur veya getir
            user, created = User.objects.get_or_create(username=f"{kullanici_adi}_{soyad}")
            
            # Kullanıcıyı giriş yapmış olarak ayarla
            login(request, user)
            
            return redirect("AdminYonetimEkrani")  # Admin paneline yönlendirin
        except Admin.DoesNotExist:
            return render(request, 'Hastane/AdminEkrani.html', {
                "error": "Kullanıcı adı veya şifre yanlış"
            })
    
    return render(request, 'Hastane/AdminEkrani.html')

def AdminYonetimEkrani(request):
    return render(request , "Hastane/AdminYonetimEkrani.html")


logger = logging.getLogger(__name__)

def DoktorEkle(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        uzmanlik = request.POST.get('uzmanlik')
        hastane = request.POST.get('hastane')

        # Basit doğrulama
        if ad and soyad and uzmanlik and hastane:
            try:
                new_doctor = Doctor.objects.create(
                    doctor_name=ad,
                    doctor_last_name=soyad,
                    speciality=uzmanlik,
                    hospital_works_in=hastane
                )
                return render(request, 'Hastane/DoktorEkle.html', {'success': True})
            except Exception as e:
                logger.error(f"Doktor kaydı sırasında bir hata oluştu: {e}")
                error_message = "Doktor kaydı sırasında bir hata oluştu."
                return render(request, 'Hastane/DoktorEkle.html', {'error_message': error_message})
        else:
            error_message = "Lütfen tüm alanları doldurun."
            return render(request, 'Hastane/DoktorEkle.html', {'error_message': error_message})

    return render(request, 'Hastane/DoktorEkle.html')
    
   

def DoktorSil(request):

    if request.method == 'POST':
        # Formdan gelen doktor id'sini al
        doktor_id = request.POST.get('doktor_id')
        
        # Doktor objesini sil
        try:
            doktor = Doctor.objects.get(pk=doktor_id)
            doktor.delete()
            return redirect('DoktorSil')  # Silme işlemi başarılıysa sayfayı yenile
        except Doctor.DoesNotExist:
            error_message = "Seçilen doktor bulunamadı."
            return render(request, 'Hastane/DoktorSil.html', {'error_message': error_message})

    # GET isteği durumunda, tüm doktorları listele
    doktorlar = Doctor.objects.all()

    return render(request, 'Hastane/DoktorSil.html', {'doktorlar': doktorlar})





def DoktorGoruntule(request):
    doktor_listesi = Doctor.objects.all()
    return render(request, 'Hastane/DoktorGoruntule.html', {'doktor_listesi': doktor_listesi})




