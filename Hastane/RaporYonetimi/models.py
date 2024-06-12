from django.contrib.auth.models import User
from django.db import models


class MedicalReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    report_date = models.DateField()
    report_content = models.TextField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medical_reports')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medical_reports_created_by')

    def __str__(self):
        return f"Report {self.report_id}"
