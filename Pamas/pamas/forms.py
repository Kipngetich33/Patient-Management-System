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

