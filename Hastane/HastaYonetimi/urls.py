from django.urls import path
from django.contrib import admin
from . import views

#http://127.0.0.1:8000/
#http://127.0.0.1:8000/Hasta
#http://127.0.0.1:8000/Doktor
#http://127.0.0.1:8000/Yonetici

urlpatterns = [
    path('HastaLogin' , views.HastaLogin),
    path('hastalistesi' , views.Hasta_listesi),
    path('hasta' , views.Hasta),
    path('BilgiGuncelle', views.BilgiGuncelle),
    path('RandevuIslemleri' ,views.RandevuIslemleri),
    path('RandevuSil' , views.RandevuSil),
    path('HastaOlustur',views.hasta_olustur),
    
    

    ]
