from django import forms


class ProfileUpdateForm(forms.Form):
    '''
    class that creates profile update form
    ''' 
    name = forms.CharField(label='Name')
    profile_pic = forms.ImageField(label = 'Profile Pic') 
    user_type = forms.IntegerField(label = 'User Type') 
    phone_number = forms.CharField(label='Phonenumber',max_length=12)
    email = forms.EmailField(label = 'email')
    hospital = forms.CharField(label = 'Hospital')
    location = forms.CharField(label = 'Location')
    

class FormAppointment(forms.Form):
    '''
    Class that creates and appointment form 
    '''
    type_of_appointment = forms.CharField(label = 'Type of appointment e.g Consultation')
    appointment_date = forms.DateField(label = 'Date  e.g 12/23/2018 ' )
    appointment_time = forms.TimeField(label = 'Time e.g 14:00')


class AttendForm(forms.Form):
    '''
    Class that creates and appointment form 
    '''
    comment = forms.CharField(label = 'Add a note', max_length=1000)
