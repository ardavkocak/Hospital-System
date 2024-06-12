from django.urls import path
from . import views

#http://127.0.0.1:8000/
#http://127.0.0.1:8000/Hasta
#http://127.0.0.1:8000/Doktor
#http://127.0.0.1:8000/Yonetici

urlpatterns = [
    path('DoktorEkrani' , views.DoktorEkrani, name="doktorekrani"),
    path('' , views.AnaEkran, name="home"),
    path('RaporEkle', views.RaporEkle, name ="raporekle"),
    path('HastaEkran', views.HastaEkran, name ="hastaekran"),
    path('DoktorRandevuEkran' ,views.DoktorRandevuEkran, name = "doktorrandevuekran"),
    path('LoginDoktor' , views.LoginDoktor, name = "logindoktor"),
    path('HastaLogin' , views.HastaLogin , name = "hastalogin"),
    path('hasta' , views.Hasta ),
    path('HastaGoruntule', views.HastaGoruntule),
    path('RaporGoruntule' , views.RaporGoruntule),
    path('RaporSil' , views.RaporSil),

]