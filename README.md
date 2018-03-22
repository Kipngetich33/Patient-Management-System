# APP NAME

### Patient Management System

## AUTHOR

Kipngetich Ngeno

## DESCRIPTION

This is a web application that allows doctors to manage their patients' data as well as allows the patients to manage appointments with their doctors.


## User stories
As a user can do the following:
* Sign in to the application 
* Crete a profile as a doctor or patient
* View profiles of their patient if its a doctor 
* Patients can view profiles of different doctors
* Patients can book, update or cancel an appointment with a doctor

## Set Up and Installation

#### Prerequisites

* Python 3.6.2
* Virtual environment
* Postgres Database
* Reliable Internet Connection

## Installation Process

* Copy repolink

in your terminal run the following commands

* $ git clone REPO-URL in your terminal
* $ cd Patient-Management-System
* $ python3.6 -m venv virtual
* $ touch .env ( to the file add :
        SECRET_KEY=<your secret key>
        DEBUG=True)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt
* $ psql ; CREATE DATABASE pamas ;

In the settings.py module of the project make the following changes

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pamas',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}

* $ python3.6 manage.py runserver (this command runs the application of port http://127.0.0.1/8000 )
 
## Known Bugs

No known bugs

## CREDITS

Moringa School,Python Documentation, StackOverflow.com and W3 schools

## Technologies Used

This project uses major technologies which are :

* HTML5/CSS
* Bootstrap
* Python3.6
* Django Frane Work
* Postgress Database

## Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through kipngetich.ngeno333@gmail.com or leave a commit here on github.

## License 

Copyright MIT [LiCENSE](./LICENSE) (c) 2017 [Kipngetich Ngeno](https://github.com/Kipngetich33)

