from django.forms import ModelForm
from pdportfolioapp.models import * 
from django import forms

class AboutMeForm(ModelForm):
    class Meta:
        model = AboutMe
        fields = ['about_me']

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['company_name', 'from_date', 'to_date', 'designation', 'description']
        exclude = ('user',)
    widgets = {
        'from_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }