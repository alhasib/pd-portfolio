from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<name>/', about_me),
    path('<name>/aboutme', about_me, name = 'about-me'),
    path('<name>/experience', experience, name = 'experience'),
    path('<name>/education', education, name = 'education'),
    path('<name>/skills', skill, name = 'skill'),
    path('<name>/interest', interest, name = 'interest'),
    path('<name>/award', award, name = 'award'),
    path('<name>/profile', profile, name = 'profile'),
    
    #admin url

    path('c-admin', c_admin_home, name = 'c_admin_home'),
    path('c-aboutme', c_about_me, name = 'c_about_me'),
    path('c-experience', c_experience, name='c_experience'),
]