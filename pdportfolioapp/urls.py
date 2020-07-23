from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('about-me', about_me, name = 'about-me'),
    path('experience', experience, name = 'experience'),
    path('education', education, name = 'education'),
    path('skills', skill, name = 'skill'),
    path('interest', interest, name = 'interest')

]