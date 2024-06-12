from django.db import models

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=20)
    doctor_last_name = models.CharField(max_length=20)
    speciality = models.CharField(max_length=30)
    hospital_works_in = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.doctor_name} {self.doctor_last_name} - {self.speciality}"
