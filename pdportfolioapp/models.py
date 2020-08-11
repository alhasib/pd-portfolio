from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AboutMe(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete = models.CASCADE)
    about_me = models.TextField()

    def __str__(self):
        return self.about_me

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 130)
    image = models.ImageField()

    def __str__(self):
        return self.name

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length = 250)
    from_date = models.DateField()
    to_date = models.DateField()
    designation = models.CharField(max_length = 250)
    description = models.TextField()

    def __str__(self):
        return self.company_name

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length = 250)
    from_date = models.DateField()
    to_date = models.DateField()
    name_of_degree = models.CharField(max_length = 250)

    def __str__(self):
        return self.name_of_degree

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 250)

    def __str__(self):
        return self.title 

class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 250)

    def __str__(self):
        return self.title
        
class Award(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 250)

    def __str__(self):
        return self.title
        