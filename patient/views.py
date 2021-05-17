from django.http import Http404
from .models import Patient
from .serializers import Patientserilizer
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

class Patient_list_create(APIView):
    
    def get(self, request, format=None):
        snippets = Patient.objects.all()
        serializer = Patientserilizer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Patientserilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Patient_update_delete(APIView):
   
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = Patientserilizer(patient)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = Patientserilizer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        patient = self.get_object(pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


 
