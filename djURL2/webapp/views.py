from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeView(request,val1,val2):
    msg=val1+" "+val2
    return HttpResponse(msg)
