from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from webapp import forms

def Empview(request):
    if request.method=='POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            print('Form Validations......!')
            print(form.cleaned_data['Name'])
            print(form.cleaned_data['Salary'])
            return HttpResponseRedirect('/Thanks')
    else:
        form=forms.EmpForm()
    return render(request,'MyApp/welcome.html',{'form':form})
def Thankview(request):
    return render(request,'MyApp/Thanks.html')
