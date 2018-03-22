from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.landing,name = 'landing'),
    url('^home/',views.home,name = 'home'),
    
]