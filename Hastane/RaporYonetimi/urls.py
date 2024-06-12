from django.urls import path
from . import views

#http://127.0.0.1:8000/
#http://127.0.0.1:8000/Hasta
#http://127.0.0.1:8000/Doktor
#http://127.0.0.1:8000/Yonetici

urlpatterns = [
    path('RaporEkle', views.rapor_ekle, name='rapor_ekle'),
    path('RaporGoruntule/<int:report_id>/', views.rapor_goruntule, name='rapor_goruntule'),
    path('RaporSil/<int:report_id>/', views.rapor_sil, name='rapor_sil'),
]