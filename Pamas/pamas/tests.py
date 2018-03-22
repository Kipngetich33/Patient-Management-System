from django.test import TestCase
from .models import Patient_profile,Doctor_profile, Appointment

class Patient_profileTestClass(TestCase):
    '''
    Class that tests the behavior of the Profile class model
    '''
    def setUp(self):
        '''
        Method that runs at the begining of each Test case
        '''
        self.test_profile = Patient_profile(email = 'doctor@gmail.com',phone_number ='0712567583', location = 'Bomet')

    def test_isinstance(self):
        '''
        Method that test if objects are instances of the class Profile
        '''
        self.assertTrue(isinstance(self.test_profile,Patient_profile))

