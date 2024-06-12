from django.shortcuts import render

def DoktorEkrani(request):
    return render(request, "Hastane/DoktorEkrani.html")

def Hasta(request):
    return render(request,"Hastane/HastaEkrani.html")

def AnaEkran(request):
    return render(request , "Hastane/GirisEkrani.html")

def RaporEkle(request):
    return render(request , "Hastane/RaporEkle.html")

def HastaEkran(request):
    return render(request , "Hastane/HastaEkran.html")

def DoktorRandevuEkran(request):
    return render(request , "Hastane/DoktorRandevuEkran.html")

def LoginDoktor(request):
    return render(request , "Hastane/LoginDoktor.html")

def HastaLogin(request):
    return render(request , "Hastane/HastaLogin.html")

def HastaGoruntule(request):
    return render(request , "Hastane/HastaGoruntule.html")

def RaporGoruntule(request):
    return render(request , "Hastane/RaporGoruntule.html")

def RaporSil(request):
    return render(request , "Hastane/RaporSil.html")