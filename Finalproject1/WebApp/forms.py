from django import forms
from WebApp.models import course
class EmpForm(forms.ModelForm):
    class Meta:
        model=course
        fields='__all__'

