from django.shortcuts import render


# Create your views here.
def home(request):
    name = 'Faizan'
    surname = 'Shaikh'

    dic = {'name': name, 'surname': surname}

    return render(request, 'MyApp/welcome.html', context=dic)
