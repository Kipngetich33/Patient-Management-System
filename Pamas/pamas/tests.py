from django.test import TestCase
from . models import Profile, Appointment

class ProfileTestClass(TestCase):
    '''
    Class that tests the behavior of the Profile class model
    '''
    def setUp(self):
        '''
        Method that runs at the begining of each Test case
        '''
        self.test_profile = Profile(name = 'Neriah' , usertype = '1' ,email = 'patient@gmail.com',phone_number ='0712567583', hospital = 'Tenwek' ,location = 'Bomet')

    def test_isinstance(self):
        '''
        Method that test if objects are instances of the class Profile
        '''
        self.assertTrue(isinstance(self.test_profile,Profile))

class AppointmentTestClass(TestCase):
    '''
    Class that tests the behavior of the Doctor_profile class model
    '''
    def setUp(self):
        '''
        Method that runs at the begining of each Test case
        '''
        self.test_profile = Appointment(type_of_appointment = 'Consultation',appointment_date = '03/23/2017', appointment_time = '7:00')

    def test_isinstance(self):
        '''
        Method that test if objects are instances of the class Appointment
        '''
        self.assertTrue(isinstance(self.test_profile,Appointment))



