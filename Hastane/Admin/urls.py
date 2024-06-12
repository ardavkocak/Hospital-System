from django.urls import path
from . import views

urlpatterns = [

    path('AdminEkrani' , views.AdminEkrani),
    path('AdminYonetimEkrani' , views.AdminYonetimEkrani),
    path('DoktorEkle' , views.DoktorEkle),
    path('DoktorSil' , views.DoktorSil),
    path('DoktorGoruntule' , views.DoktorGoruntule),
    path('HastaSil' , views.HastaSil)


]