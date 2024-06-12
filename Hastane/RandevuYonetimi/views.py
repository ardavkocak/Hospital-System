from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from .models import Appointment
from DoktorYonetimi.models import Doctor
from HastaYonetimi.models import Patient
import logging
from django.db import connection

logger = logging.getLogger(__name__)

def RandevuEkle(request):
    if request.method == 'POST':
        hasta_id = request.POST.get('hasta')
        doktor_id = request.POST.get('doktor')
        randevu_tarihi = request.POST.get('randevu_tarihi')
        randevu_saati = request.POST.get('randevu_saati')

        try:
            hasta = get_object_or_404(Patient, patient_id=hasta_id)
            doktor = get_object_or_404(Doctor, doctor_id=doktor_id)
            new_appointment = Appointment.objects.create(
                patient=hasta,
                doctor=doktor,
                appointment_date=randevu_tarihi,
                appointment_time=randevu_saati,
            )
            messages.success(request, "Randevu başarıyla oluşturuldu.")
            return redirect('randevulistesi')
        except Patient.DoesNotExist:
            messages.error(request, "Geçersiz hasta seçimi.")
        except Doctor.DoesNotExist:
            messages.error(request, "Geçersiz doktor seçimi.")
        except Exception as e:
            logger.error(f"Randevu oluşturulurken bir hata oluştu: {e}")
            messages.error(request, f"Randevu oluşturulurken bir hata oluştu: {e}")

    hastalar = Patient.objects.all()
    doktorlar = Doctor.objects.all()
    return render(request, 'Hastane/RandevuEkle.html', {'hastalar': hastalar, 'doktorlar': doktorlar})


def RandevuGoruntule(request):

    randevular = Appointment.objects.all()

    return render(request , "Hastane/RandevuGoruntule.html",{'randevular': randevular}) 

#def RandevuGoruntuleozel(request):
    patient_name = request.GET.get('patient_name')

    if patient_name:
        query = """
        SELECT a.appointment_id, a.appointment_date, a.appointment_time, 
               p.patient_name, p.patient_last_name, 
               d.doctor_name, d.doctor_last_name 
        FROM Hastane_appointment a
        JOIN HastaYonetimi_patient p ON a.patient_id = p.patient_id
        JOIN DoktorYonetimi_doctor d ON a.doctor_id = d.doctor_id
        WHERE CONCAT(p.patient_name, ' ', p.patient_last_name) = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [patient_name])
            randevular = cursor.fetchall()
    else:
        randevular = []

    return render(request, "Hastane/RandevuGoruntule.html", {'randevular': randevular})




def RandevuSil(request):
    if request.method == 'POST':
        randevu_id = request.POST.get("randevu_id")
        try:
            randevu = Appointment.objects.get(appointment_id=randevu_id)
            randevu.delete()
            messages.success(request, "Randevu başarıyla silindi.")
        except Appointment.DoesNotExist:
            messages.error(request, "Geçersiz randevu ID.")
        except Exception as e:
            messages.error(request, f"Randevu silinirken bir hata oluştu: {e}")

    return render(request, 'Hastane/RandevuSil.html')
    

