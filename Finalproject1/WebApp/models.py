from django.db import models

# Create your models here.
class course(models.Model):
    Course_ID=models.IntegerField()
    Course_Name=models.CharField(max_length=20)
    Course_Fees=models.IntegerField()
    Course_Duration=models.CharField(max_length=20)
