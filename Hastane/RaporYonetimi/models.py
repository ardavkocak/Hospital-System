from django.db import models

class MedicalReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    report_date = models.DateField()
    report_content = models.TextField()

    def __str__(self):
        return f"Report {self.report_id}"
