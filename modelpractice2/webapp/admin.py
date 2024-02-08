from django.contrib import admin
from webapp.models import Emp


# Register your models here.
class Empadmin(admin.ModelAdmin):
    list_display = ['empid', 'empname', 'empsal', 'empadd']


admin.site.register(Emp, Empadmin)
