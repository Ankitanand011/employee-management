from django.db import models
from django.db.models import Q

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    salary = models.IntegerField()
    email = models.EmailField()
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="employees"
    )

    def __str__(self):
        return super().__str__()