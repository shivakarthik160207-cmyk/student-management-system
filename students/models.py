from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    student_id = models.CharField(max_length=20)

    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)


    def __str__(self):
        return self.name