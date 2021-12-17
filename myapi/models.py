# models.py
from django.db import models
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=80)
    designation = models.CharField(max_length=80)
    salary = models.IntegerField()
    def __str__(self):
        return self.name