from typing import Any
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

    def __int__(self):
        return self.name


class Students(models.Model):
    full_name = models.CharField(max_length=100)
    phone_numbers = models.CharField(max_length=13)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __int__(self):
        return f'{self.full_name}  {self.phone_numbers}'


class Attendance(models.Model):
    is_present = models.BooleanField(default=True)
    students = models.ForeignKey(Students, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __int__(self):
        return f'{self.created_at}  {self.is_present}'
