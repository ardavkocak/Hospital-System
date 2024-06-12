from django.urls import path
from django.contrib import admin
from . import views

#http://127.0.0.1:8000/
#http://127.0.0.1:8000/Hasta
#http://127.0.0.1:8000/Doktor
#http://127.0.0.1:8000/Admin

urlpatterns = [
    path('HastaLogin' , views.HastaLogin),
    path('hastalistesi' , views.Hasta_listesi, name="hastalistesi"),
    path('hasta' , views.Hasta , name="hasta"),
    path('BilgiGuncelle/<int:patient_id>/', views.BilgiGuncelle, name='bilgiguncelle'),
    path('HastaOlustur',views.hasta_olustur),
    path('Hastacikart', views.hasta_sil, name="hastacikart"),
    
    

    ]
