from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('patient_list_create/', views.Patient_list_create.as_view(),name='patient_list_create'),
    path('patient_update_delete/<int:pk>',views.Patient_update_delete.as_view(),name='patient_update_delete'),
]