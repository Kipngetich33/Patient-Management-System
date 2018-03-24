from rest_framework import serializers
from . models import Profile,Appointment

class profileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'