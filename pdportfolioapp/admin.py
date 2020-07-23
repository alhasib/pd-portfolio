from django.contrib import admin

# Register your models here.

from .models import * 
admin.site.register(AboutMe)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Interest)