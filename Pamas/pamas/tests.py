from django.test import TestCase
from .models import Profile,Appointment

class ProfileTestClass(TestCase):
    '''
    Class that tests the behavior of the Profile class model
    '''
    def setUp(self):
        '''
        Method that runs at the begining of each Test case
        '''
        self.test_profile = Profile(user_type = '1',email = 'doctor@gmail.com',hospital= 'Tenwek Hospital', location = 'Bomet')

    def test_isinstance(self):
        '''
        Method that test if objects are instances of the class Profile
        '''
        self.assertTrue(isinstance(self.test_profile,Profile))

