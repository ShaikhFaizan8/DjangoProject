from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    return HttpResponse("<a href='/hii'>hi</a>")
def myview(request):
    return HttpResponseRedirect(reverse('bye'))
def byeview(request):
    return HttpResponse("<a href='/hello'>Good....bye</a>")
def page(request):
    return HttpResponseRedirect(reverse('i'))
def lastpage(request):
    return HttpResponse("<h1 style=color:red;text-align:center>Yeah Great Now Go Back</h1>")

