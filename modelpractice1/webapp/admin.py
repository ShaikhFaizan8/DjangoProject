from django.contrib import admin
from webapp.models import Emp


# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['empid','empname']


admin.site.register(Emp, EmpAdmin)
