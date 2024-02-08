from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request,val1,val2):
    f=val1+" "+val2
    return HttpResponse(f)