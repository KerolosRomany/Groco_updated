from django.contrib import admin
from .models import UserProfile, PersonalInfo

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(PersonalInfo)
