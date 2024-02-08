# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .forms import SignupForm
from .models import Public


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Check if the username already exists
            username = form.cleaned_data['username']
            if Public.objects.filter(username=username).exists():
                # Username already exists, handle this case (e.g., display an error message)
                return render(request, 'signup.html', {'form': form,
                                                       'error_message': 'Username already exists. Please choose a different one.'})

            # Create a new user
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Public.objects.create(username=username, email=email, password=make_password(password))
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})
# WebApp/views.py
from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
# WebApp/views.py
from django.shortcuts import render

def dashboard_view(request):
    # Your dashboard logic here
    return render(request, 'dashboard.html')


