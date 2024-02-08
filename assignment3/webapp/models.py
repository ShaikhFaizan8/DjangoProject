from django.db import models
class Students2(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Course = models.CharField(max_length=20)
    Location = models.CharField(max_length=20)