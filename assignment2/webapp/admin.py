from django.contrib import admin
from webapp.models import Students

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['ID','Name','Age','Course','Location']
admin.site.register(Students,StudentAdmin)
