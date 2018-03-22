from django.contrib import admin
from .models import Patient_profile, Doctor_profile,Appointment

admin.site.register(Doctor_profile)
admin.site.register(Patient_profile)
admin.site.register(Appointment)