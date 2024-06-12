from django.urls import path
from . import views

#http://127.0.0.1:8000/
#http://127.0.0.1:8000/Hasta
#http://127.0.0.1:8000/Doktor
#http://127.0.0.1:8000/Yonetici

urlpatterns = [
    path('DoktorEkrani' , views.DoktorEkrani, name="doktorekrani"),
    path('' , views.AnaEkran, name="home"),
    path('HastaEkran', views.HastaEkran, name ="hastaekran"),
    path('LoginDoktor' , views.LoginDoktor, name = "logindoktor"),
    path('HastaLogin' , views.HastaLogin , name = "hastalogin"),
   
   

]