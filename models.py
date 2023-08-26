from django.db import models

# Create your models here.
class TeacherModel(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    uname=models.EmailField()
    password=models.CharField(max_length=30)
    contact=models.IntegerField()