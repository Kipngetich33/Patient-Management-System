from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length =30 , null = True)
    profile_pic = models.ImageField(upload_to="images/",null = True)
    user_type = models.CharField(max_length =30 , null = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    email = models.EmailField(null = True)
    hospital = models.CharField(max_length =30 , null = True)
    location = models.CharField(max_length =30) 

    def __str__(self):
        return self.email 

    @classmethod
    def get_doctors(cls):
        '''
        Method that returns all the available doctors
        '''
        found_doctors = cls.objects.filter(user_type = 1)
        return found_doctors

    @classmethod
    def find_profile(cls,name):
        found_profiles = cls.objects.filter(name__icontains = name).all()
        return found_profiles


# this is the APIs section 
class Appointment(models.Model):
    type_of_appointment = models.CharField(max_length =30)
    appointment_date = models.DateField(null = True)
    appointment_time = models.TimeField(null = True)
    pub_date = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Profile,on_delete=models.CASCADE)
    patient = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(default = False)
    on = models.BooleanField(default = True)

    def __str__(self):
        return self.type_of_appointment


