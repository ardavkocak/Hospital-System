from django.db import models
from datetime import datetime


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=30)
    patient_last_name = models.CharField(max_length=20)
    p_birth_date = models.DateField()
    p_gender = models.CharField(max_length=1)
    phone_number = models.CharField(max_length=11)
    p_address = models.TextField()

    





