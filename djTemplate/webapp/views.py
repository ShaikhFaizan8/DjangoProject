from django.shortcuts import render

# Create your views here.
def welcomeviews(request):
    return render(request,'MyApp/welcome.html')
def thankviews(request):
    return render(request,'Myapp/thank.html')
