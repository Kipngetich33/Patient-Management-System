from rest_framework import serializers
from . models import Doctor_profile, Patient_profile, Appointment

class Doctor_profileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor_profile
        fields = '__all__'

class Patient_profileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient_profile
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'