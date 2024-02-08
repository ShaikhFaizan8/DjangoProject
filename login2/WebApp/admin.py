# myapp/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Public

class CustomUserAdmin(UserAdmin):
    model = Public
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

admin.site.register(Public, CustomUserAdmin)
