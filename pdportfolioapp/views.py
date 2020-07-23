from django.shortcuts import render
from .models import *
# Create your views here.
def about_me(request):
    about = AboutMe.objects.all()
    context = {"about":about}
    return render(request, 'about_me.html', context)


def experience(request):
    experience = Experience.objects.all()
    context = {'experience': experience}
    return render(request, 'experience.html', context)

def education(request):
    education = Education.objects.all()
    context = {'education':education}
    return render(request, 'education.html', context)

def skill(request):
    all_skill = Skill.objects.all()
    context = {"skill":all_skill}
    return render(request, 'skill.html', context)


def interest(request):
    all_interest = Interest.objects.all()
    context = {'interest': all_interest}
    return render(request, 'interest.html', context)