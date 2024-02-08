from django.shortcuts import render

# Create your views here.
from datetime import datetime

def dateInfo(request):
    dd=datetime.now()

    hours=int(dd.strftime('%H'))

    if hours<12:
        msg='GOOD MORNING'
    elif hours<16:
        msg='GOOD AFTERNOON'
    else:
        msg='GOOD NIGHT'

    dic={'wish':msg}

    return render(request,'MyApp/welcom.html',context=dic)
