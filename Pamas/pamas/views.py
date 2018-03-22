from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Doctor_profile,Patient_profile,Appointment
from . serializers import Doctor_profileSerializer, Patient_profileSerializer,AppointmentSerializer

from django.contrib.auth.decorators import login_required
from .permissions import IsAdminOrReadOnly

#Create your views here.
def landing(request):
    title = "landing Page"
    return render(request,'base/landing.html',{"title":title})

@login_required(login_url='/accounts/login/')
def home(request):
    title = 'Home'
    return render(request,'base/home.html',{"title":title})

@login_required(login_url='/accounts/login/')
def appointment(request):
    title = 'Appointment'
    doctors = Doctor_profile.get_doctors()
    return render(request,'base/appointment.html',{"title":title,"doctors":doctors})



# these are the API view classes
class doctor_list(APIView):
    def get(self, request, format=None):
        all_doctors = Doctor_profile.objects.all()
        serializers = Doctor_profileSerializer(all_doctors, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = Doctor_profileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAdminOrReadOnly,)

class patients_list(APIView):
    def get(self, request, format=None):
        all_patients = Patient_profile.objects.all()
        serializers = Patient_profileSerializer(all_patients, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = Patient_profileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAdminOrReadOnly,)

class appointments_list(APIView):
    def get(self, request, format=None):
        all_appointments = Appointment.objects.all()
        serializers = AppointmentSerializer(all_appointments, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = AppointmentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAdminOrReadOnly,)


