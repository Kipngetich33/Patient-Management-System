from django.test import TestCase
from .models import Patient_profile,Doctor_profile, Appointment

class Patient_profileTestClass(TestCase):
    '''
    Class that tests the behavior of the Patient_rofile class model
    '''
    def setUp(self):
        '''
        Method that runs at the begining of each Test case
        '''
        self.test_profile = Patient_profile(email = 'patient@gmail.com',phone_number ='0712567583', location = 'Bomet')

    def test_isinstance(self):
        '''
        Method that test if objects are instances of the class Profile
        '''
        self.assertTrue(isinstance(self.test_profile,Patient_profile))

class Doctor_profileTestClass(TestCase):
    '''
    Class that tests the behavior of the Doctor_profile class model
    '''
    def setUp(self):
        '''
        Method that runs at the begining of each Test case
        '''
        self.test_profile = Doctor_profile(email = 'doctor@gmail.com',phone_number ='0712567583',hospital ='Aga Khan' ,location = 'Bomet')

    def test_isinstance(self):
        '''
        Method that test if objects are instances of the class Profile
        '''
        self.assertTrue(isinstance(self.test_profile,Doctor_profile))

    def test_get_doctors(self):
        '''
        Method that tests the get doctors method of Doctor_profile class
        '''
        self.test_profile.save()
        found_doctors = Doctor_profile.get_doctors()
        self.assertTrue(len(found_doctors) == 1)


