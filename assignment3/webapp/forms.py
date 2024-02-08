from django import forms
from webapp.models import Students2
class EmpForm2(forms.ModelForm):
    class Meta:
        model=Students2
        fields='__all__'

