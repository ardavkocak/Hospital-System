from django.urls import path
from . import views

#http://127.0.0.1:8000/
#http://127.0.0.1:8000/Hasta
#http://127.0.0.1:8000/Doktor
#http://127.0.0.1:8000/Yonetici

urlpatterns = [
    
   
    path('RandevuGoruntule' , views.RandevuGoruntule, name="randevulistesi"),
    path('RandevuSil' , views.RandevuSil),
    path('RandevuEkle', views.RandevuEkle, name ="raporekle"),
    
]