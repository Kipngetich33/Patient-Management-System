from django.shortcuts import render, redirect
from . forms import ProfileUpdateForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Profile,Appointment
from . serializers import profileSerializer,AppointmentSerializer

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
    doctors = Profile.get_doctors()
    return render(request,'base/appointment.html',{"title":title,"doctors":doctors})

# these are the test profiles and update_profiles

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user 
    title = 'Update Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.name = form.cleaned_data['name']
                requested_profile.profile_pic = form.cleaned_data['name']
                requested_profile.user_type = form.cleaned_data['user_type']
                requested_profile.phone_number = form.cleaned_data['phone_number']
                requested_profile.email = form.cleaned_data['email']
                requested_profile.hospital = form.cleaned_data['hospital']
                requested_profile.location = form.cleaned_data['location']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUpdateForm()
    except:
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(name = form.cleaned_data['name'], profile_pic= form.cleaned_data['profile_pic'],user_type = form.cleaned_data['user_type'],phone_number = form.cleaned_data['phone_number'],email = form.cleaned_data['email'],hospital = form.cleaned_data['hospital'],location = form.cleaned_data['location'],user = current_user)
                new_profile.save()
                return redirect( profile )
        else:
            form = ProfileUpdateForm()

    return render(request,'profile/update_profile.html',{"title":title,"current_user":current_user,"form":form})

@login_required(login_url='/accounts/login/')
def profile(request):
    title = 'Profile'
    current_user = request.user
    try:
        profile = Profile.objects.get(user_id = current_user)
    except:
        profile = Profile.objects.get(user = 'default_user')
    return render(request, 'profile/profile.html',{"profile":profile,"current_user":current_user,"following":following,"followers":followers})



# these are the API view classes

class profiles_list(APIView):
    def get(self, request, format=None):
        all_patients = Profile.objects.all()
        serializers = profileSerializer(all_patients, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = profileSerializer(data=request.data)
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




