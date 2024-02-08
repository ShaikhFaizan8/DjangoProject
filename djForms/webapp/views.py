from django.shortcuts import render
from webapp import Forms
# Create your views here.
def EmpView(request):
    form=Forms.EmpForm()

    return render(request,'MyApp/welcome.html',{'form':form})