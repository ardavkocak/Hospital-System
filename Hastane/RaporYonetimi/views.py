from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MedicalReport
from datetime import date

def rapor_ekle(request):
    if request.method == 'POST':
        report_date = request.POST.get('report_date')
        report_content = request.POST.get('report_content')
        file_url = request.POST.get('file_url', '')

        if report_content:
            try:
                new_report = MedicalReport(
                    report_date=report_date,
                    report_content=report_content,
                    file_url=file_url
                )
                new_report.save()
                messages.success(request, "Rapor başarıyla eklendi.")
                return redirect('rapor_goruntule', report_id=new_report.report_id)
            except Exception as e:
                messages.error(request, f"Rapor ekleme sırasında bir hata oluştu: {e}")
        else:
            messages.error(request, "Lütfen rapor içeriğini giriniz.")
    
    return render(request, "Hastane/rapor_ekle.html")

def rapor_goruntule(request, report_id):
    report = get_object_or_404(MedicalReport, report_id=report_id)
    return render(request, 'Hastane/rapor_goruntule.html', {'report': report})

def rapor_sil(request, report_id):
    report = get_object_or_404(MedicalReport, report_id=report_id)
    
    if request.method == 'POST':
        try:
            report.delete()
            messages.success(request, "Rapor başarıyla silindi.")
            return redirect('rapor_listesi')
        except Exception as e:
            messages.error(request, f"Rapor silinirken bir hata oluştu: {e}")

    return render(request, 'Hastane/rapor_sil.html', {'report': report})
