from django.shortcuts import render
from WebApp import forms
from django.http import HttpResponseRedirect
# Create your views here.
def Home_View(request):
    return render(request,'MyApp/home.html')
def Courses_View(request):
    return  render(request,'MyApp/courses.html')
def About_View(request):
    return  render(request,'MyApp/about.html')
def Contact_View(request):
    return  render(request,'MyApp/contact.html')

def Login_View(request):
    return  (request,'MyApp/login.html')


def Thank_View(request):
    return  render(request,'MyApp/thanks.html')


def Emp_View(request):
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/thanks')  # Redirect to a success page or any other page after successful submission
    else:
        form =forms.EmpForm()

    return render(request,'MyApp/courses.html',{'form': form})








