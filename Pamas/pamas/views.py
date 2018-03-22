from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Doctor_profile,Patient_profile,Appointment
from . serializers import Doctor_profileSerializer, Patient_profileSerializer,AppointmentSerializer
from django.contrib.auth.decorators import login_required

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





































# class doctor_list(APIView):
    
#     def get(self,request):
#         doctors1 = Doctor_profile.objects.all()
#         serializer = Doctor_profileSerializer(doctors1, many = True)
#         return Response(serializer.data)
        
    
#     def post(self):
#         pass
        
# class patient_list(APIView):
    
#     def get(self,request):
#         patient1 = Patient_profile.objects.all()
#         serializer = Patient_profileSerializer(patient1, many = True)
#         return Response(serializer.data)
        
    
#     def post(self):
#         pass

# class appointment_list(APIView):
    
#     def get(self,request):
#         appointment1 = Appointment.objects.all()
#         serializer = AppointmentSerializer(appointment1, many = True)
#         return Response(serializer.data)
        
    
#     def post(self):
#         pass




