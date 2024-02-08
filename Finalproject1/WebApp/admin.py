from django.contrib import admin
from WebApp.models import course

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Course_ID','Course_Name','Course_Fees','Course_Duration']
admin.site.register(course,StudentAdmin)
