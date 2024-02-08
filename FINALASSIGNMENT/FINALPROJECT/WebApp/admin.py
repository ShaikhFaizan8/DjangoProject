from django.contrib import admin
from WebApp.models import Students
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['CourseId','CourseName','CourseFees','CourseDuration',]
admin.site.register(Students,StudentAdmin)