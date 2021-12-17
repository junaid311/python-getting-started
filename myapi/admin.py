from django.contrib import admin

# Register your models here.

from .models import Employee, Hero
admin.site.register(Hero)
admin.site.register(Employee)
