from django.db import models

class Profile(models.Model):
    user_type = model.IntegerField
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    hospital = models.CharField(max_length =30)
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.first_name

class Appointment(models.Model):
    type_of_appointment = models.CharField(max_length =30)
    appointement_time = models.CharField(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(User,on_delete=models.CASCADE)
    patient = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(default = False)

    def __str__(self):
        return self.type_of_appointment


