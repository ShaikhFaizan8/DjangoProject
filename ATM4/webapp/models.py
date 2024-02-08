from django.db import models

# Create your models here.
class Students(models.Model):
    Rollno=models.IntegerField()
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Course=models.CharField(max_length=20)
    Location=models.CharField(max_length=20)