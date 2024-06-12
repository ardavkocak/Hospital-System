from django.db import models

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=20)
    admin_last_name = models.CharField(max_length=20)
    # Diğer alanlar eklenebilir

    def __str__(self):
        return f"{self.admin_name} {self.admin_last_name}"
