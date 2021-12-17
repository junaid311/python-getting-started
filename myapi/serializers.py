# serializers.py
from django.db.models import fields
from rest_framework import serializers

from .models import Hero

from .models import Employee

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'designation', 'salary')