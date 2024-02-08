from django.shortcuts import render
from webapp import forms
from django.http import HttpResponseRedirect

# Create your views here.
def ThankView(request):
    return render(request,'MyApp/Thanks.html')
def Homeview(request):
    return render(request,'MyApp/Home.html')

def AboutUsview(request):
    return render(request,'MyApp/Aboutus.html')
def Emp_View(request):
    if request.method=='POST':
        form=forms.EmpForm2(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/thanks')
    else:
        form=forms.EmpForm()
        return render(request,'MyApp/Reg.html',{'form':form})


