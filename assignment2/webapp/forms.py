from django import forms
from webapp.models import Students
class EmpForm(forms.ModelForm):
    class Meta:
        model=Students
        fields='__all__'

