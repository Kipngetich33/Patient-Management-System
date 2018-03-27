from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.landing,name = 'landing'),
    url('^home/',views.home,name = 'home'),
    url('^appointment/',views.appointment,name = 'appointment'),
    url('^profile/',views.profile,name = 'profile'),
    url('^update/profile/',views.update_profile,name = 'update_profile'),
    url('^search/results',views.search_results,name = 'search_results'),
    url('^book/appointment/(\d+)',views.book_appointment,name = 'book_appointment'),
    url('^my/appointments/',views.my_appointment,name = 'my_appointment'),
    url('^attend/appointment/(\d+)',views.attend_appointment,name = 'attend_appointment'),
    url('^cancel/appointment/(\d+)',views.cancel_appointment,name = 'cancel_appointment'),
     url('^view/profile/(\d+)',views.view_profile,name = 'view_profile'),
    url(r'^api/profiles/$', views.profiles_list.as_view()),
    url(r'^api/appointments/$', views.appointments_list.as_view())
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)