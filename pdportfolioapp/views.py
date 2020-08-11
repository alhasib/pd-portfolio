from django.shortcuts import render
from django.http import response
from .models import *
from pdportfolioapp.forms import *
# Create your views here.



def about_me(request, name):
    about = AboutMe.objects.get(user__username = name)
    profile = Profile.objects.get(user__username = name)
    context = {"about":about, 'profile':profile}
    return render(request, 'about_me.html', context)


def experience(request, name):
    profile = Profile.objects.get(user__username = name)
    experience = Experience.objects.filter(user__username = name)
    context = {'experience': experience, 'profile':profile}
    return render(request, 'experience.html', context)

def education(request, name):
    profile = Profile.objects.get(user__username = name)
    education = Education.objects.filter(user__username = name)
    context = {'education':education, 'profile':profile}
    return render(request, 'education.html', context)

def skill(request, name):
    profile = Profile.objects.get(user__username = name)
    all_skill = Skill.objects.filter(user__username = name)
    context = {"skill":all_skill, 'profile':profile}
    return render(request, 'skill.html', context)


def interest(request, name):
    profile = Profile.objects.get(user__username = name)
    all_interest = Interest.objects.filter(user__username = name)
    context = {'interest': all_interest, 'profile':profile}
    return render(request, 'interest.html', context)

def award(request, name):
    profile = Profile.objects.get(user__username = name)
    award = Award.objects.filter(user__username = name)
    context = {'award':award, 'profile':profile}
    return render(request, 'award.html', context)

def profile(request, name):
    profile = Profile.objects.get(user__username = name)
    context = {'profile':profile}
    return render(request, 'profile.html', context)


    # admin view


def c_admin_home(request):
    return render(request, 'c_admin_home.html')

# def c_about_me(request):
#     return render(request, 'c_about_me.html')

# add view

def c_about_me(request):
    # print("hasib")
    if request.method == 'POST':
        form = AboutMeForm(request.POST)
        if form.is_valid:
            form = form.save(commit = False)
            form.user = request.user
            print(form.about_me)
            print(request.user.username)
            form.save()
            form = AboutMeForm()
            context = {'form':form}
            return render(request, 'c_about_me.html', context)
    else:      
        form = AboutMeForm()
        context = {'form':form}
        return render(request, 'c_about_me.html', context)

def c_experience(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid:
            form = form.save(commit = False)
            form.user = request.user 
            form.save()
            form = ExperienceForm()
            context = {'form':form}
            return render(request, 'c_experience.html', context)
    form = ExperienceForm()
    context = {'form':form}
    return render(request, 'c_experience.html', context)
