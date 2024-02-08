from django.db import models


# Create your models here.
class Emp(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(max_length=30)
    empsal = models.IntegerField()
    empadd = models.CharField(max_length=30)




