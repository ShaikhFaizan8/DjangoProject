from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def homepage(request):
    return HttpResponse("<h1 style='text-align:center;color:red'>Hello I am Faizan</h1>")
def home(request,id):
    return HttpResponse(f"How Are You {id}")