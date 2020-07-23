from django.db import models

# Create your models here.

class AboutMe(models.Model):
    about_me = models.TextField()

    def __str__(self):
        return self.about_me

    

class Experience(models.Model):
    company_name = models.CharField(max_length = 250)
    from_date = models.DateField()
    to_date = models.DateField()
    designation = models.CharField(max_length = 250)
    description = models.TextField()

    def __str__(self):
        return self.company_name

class Education(models.Model):
    institution_name = models.CharField(max_length = 250)
    from_date = models.DateField()
    to_date = models.DateField()
    name_of_degree = models.CharField(max_length = 250)

    def __str__(self):
        return self.name_of_degree

class Skill(models.Model):
    title = models.CharField(max_length = 250)

    def __str__(self):
        return self.title 

class Interest(models.Model):
    title = models.CharField(max_length = 250)

    def __str__(self):
        return self.title
        

        