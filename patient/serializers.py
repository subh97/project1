from  rest_framework import serializers
from .models import Patient

class Patientserilizer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=['patient_regNo','patient_name','patient_email','patient_mobile','admitted_at']

    