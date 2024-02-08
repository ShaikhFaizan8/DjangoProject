from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,<a href='myapp/hello.html'>click here</a>)
def hi(request):
    return render(request,'myapp/hi.html')