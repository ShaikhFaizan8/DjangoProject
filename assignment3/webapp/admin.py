from django.contrib import admin
from webapp.models import Student2


# Register your models here.
class StudentAdmin2(admin.ModelAdmin):
    list_display = ['Name', 'Age', 'Course', 'Location']


admin.site.register(Student2,StudentAdmin2)
