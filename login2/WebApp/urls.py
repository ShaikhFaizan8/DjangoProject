# myapp/urls.py
# WebApp/urls.py
from django.urls import path
from .views import login_view, signup_view, dashboard_view  # Import the correct functions

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('dashboard/', dashboard_view, name='dashboard'),
    # Add more URLs as needed
]
