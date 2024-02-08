from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def homeView(request):
    return HttpResponse("Home Page")
def indexView(request,id):
    return HttpResponse(f'Index Page {id}')