from django.shortcuts import render


def Randevu(request):
    return render(request, "Hastane/randevu.html")

