from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def homeviews(request):
    return HttpResponse("<a href='/Hyperlink.html'>Click Here</a>")
def pageviews(request):
    return HttpResponseRedirect (reverse('hello'))
def lastpage(request):
    return HttpResponseRedirect ('Who r you ?')



