from django.shortcuts import render

# Create your views here.
def Homeview(request):
    return render(request,'MyApp/Home.html')
def Servicesview(request):
    return render(request,'MyApp/Services.html')
def AboutUsview(request):
    return render(request,'MyApp/About Us.html')
def Contactview(request):
    return render(request,'MyApp/Contact.html')
