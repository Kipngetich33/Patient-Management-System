from django.shortcuts import render, redirect
from . forms import ProfileUpdateForm, FormAppointment, AttendForm

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
    current_user = request.user
    title = 'Home'
    return render(request,'base/home.html',{"title":title,"current_user":current_user})

@login_required(login_url='/accounts/login/')
def appointment(request):
    title = 'Appointments'
    doctors = Profile.get_doctors()
    patients = Profile.get_patients()
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
            fname = f'{current_user.username}'

            if form.is_valid():
                requested_profile.name = form.cleaned_data['name']
                requested_profile.profile_pic = form.cleaned_data['profile_pic']
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
                new_profile = Profile(profile_pic= form.cleaned_data['profile_pic'],user_type = form.cleaned_data['user_type'],phone_number = form.cleaned_data['phone_number'],email = form.cleaned_data['email'],hospital = form.cleaned_data['hospital'],location = form.cleaned_data['location'],user = current_user)
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
        profile = Profile.objects.get(user = current_user)
    except:
        profile = Profile.objects.get(email = 'default_user@pamas.com')
    return render(request, 'profile/profile.html',{"profile":profile,"current_user":current_user})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'name' in request.GET and request.GET["name"]: 
        search_name = request.GET.get("name")
        found_users = Profile.find_profile(search_name)
        message =f"{search_name}" 

        return render(request,'base/search_results.html',{"message":message,"found_users":found_users})
    else:
        message = "Please enter a valid username"
    return render(request,'base/search_results.html',{"message":message})

@login_required(login_url='/accounts/login/')
def book_appointment(request,doc_id):
    current_user = request.user 
    title = 'Book Appointment'
    requested_doctor = Profile.objects.get(id = doc_id)
    if request.method == 'POST':
        form = FormAppointment(request.POST,request.FILES)
        fname = f'{current_user.username}'

        if form.is_valid():
            type_of_appointment = form.cleaned_data['type_of_appointment']
            appointment_date = form.cleaned_data['appointment_date']
            appointment_time = form.cleaned_data['appointment_time']

            new_appointment = Appointment(type_of_appointment = type_of_appointment ,appointment_date = appointment_date, appointment_time = appointment_time, doctor =requested_doctor ,patient = current_user)
            new_appointment.save()
            return redirect( 'home' )
    else:
        form = FormAppointment()
    return render(request,'base/book_appointment.html',{"form":form})


def my_appointment(request):
    current_user = request.user 
    my_appointments = Appointment.find_my_appointment(current_user)
    attended = Appointment.find_attended_or_cancelled(current_user)
    return render(request,'base/my_appointment.html',{"my_appointments":my_appointments,"attended":attended})

def attend_appointment(request,appointment_id):
    title = 'Attend Appointment'
    current_user = request.user
    requested_appointment = Appointment.objects.get(id = appointment_id)
    if request.method == 'POST':
        form = AttendForm(request.POST,request.FILES)
        fname = f'{current_user.username}'

        if form.is_valid():
            comment = form.cleaned_data['comment']
            requested_appointment.status = True # the status is set to true once the appointment has been attended
            requested_appointment.on = 'Attended' 
            requested_appointment.save()
            return redirect( 'my_appointment' )
    else:
        form = AttendForm()
    return render(request,'base/attend_appointment.html',{"form":form,"requested_appointment":requested_appointment})

def cancel_appointment(request,appointment_id):
    requested_appointment = Appointment.objects.get(id = appointment_id)
    requested_appointment.status = True
    requested_appointment.on = 'Cancelled' # on is set to false if the appointment is cancelled
    requested_appointment.save()
    return redirect('my_appointment')

@login_required(login_url='/accounts/login/')
def view_profile(request,user_id):
    title = 'Profile'
    try:
        profile = Profile.objects.get(id = user_id)
        current_user = profile.name
    except:
        profile = Profile.objects.get(email = 'default_user@pamas.com')
    return render(request, 'profile/profile.html',{"profile":profile,"current_user":current_user})

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






