from django.db import models

class Student(models.Model):

    name=models.CharField(max_length=100)

    usn=models.CharField(max_length=20)

    semester=models.IntegerField()

    status=models.CharField(max_length=20)