from django.db import models

# Create your models here.
class Emp(models.Model):
    Eid=models.IntegerField()
    Name=models.CharField(max_length=20)
    Salary=models.IntegerField()
    Location=models.CharField(max_length=20)
    Position=models.CharField(max_length=20)