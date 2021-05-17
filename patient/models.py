
from django.db import models
from datetime import datetime

class Patient(models.Model):
    patient_regNo=models.CharField(primary_key=True,max_length=10)
    patient_name=models.CharField(max_length=65)
    patient_email=models.EmailField()
    patient_mobile=models.TextField(max_length=10)
    admitted_at =models.DateTimeField(default=datetime.now())




# Create your models here.


# Create your models here.
