from django.db import models

class Students(models.Model):
    CourseId = models.IntegerField()
    CourseName = models.CharField(max_length=20)
    CourseFees = models.IntegerField()
    CourseDuration= models.IntegerField()


