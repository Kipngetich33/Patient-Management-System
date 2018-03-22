from django.db import models
from django.contrib.auth.models import User

class Patient_profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.IntegerField
    email = models.EmailField()
    hospital = models.CharField(max_length =30)
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.email

class Doctor_profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.IntegerField
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.email

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


