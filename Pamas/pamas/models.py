from django.db import models
from django.contrib.auth.models import User


class Patient_profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    email = models.EmailField(null = True)
    hospital = models.CharField(max_length =30 , null = True)
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.email

class Doctor_profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    email = models.EmailField(null = True)
    phone_number = models.IntegerField(null = True)
    location = models.CharField(max_length =30, null = True)
    hospital = models.CharField(max_length =30, null = True)

    def __str__(self):
        return self.email

    @classmethod
    def get_doctors(cls):
        '''
        Method that returns all the available doctors
        '''
        found_doctors = Doctor_profile.objects.all()
        return found_doctors

class Appointment(models.Model):
    type_of_appointment = models.CharField(max_length =30)
    appointement_time = models.CharField(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor_profile,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient_profile,on_delete=models.CASCADE)
    status = models.BooleanField(default = False)
    on = models.BooleanField(default = True)

    def __str__(self):
        return self.type_of_appointment


