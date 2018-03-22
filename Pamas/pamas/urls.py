from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.landing,name = 'landing'),
    url('^home/',views.home,name = 'home'),
    url('^appointment/',views.appointment,name = 'appointment'),
    url(r'^api/doctors/$', views.doctor_list.as_view()),
    url(r'^api/patients/$', views.patients_list.as_view()),
    url(r'^api/appointments/$', views.appointments_list.as_view())

    
]