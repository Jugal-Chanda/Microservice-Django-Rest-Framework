from django.contrib import admin
from django.urls import path
from accounts.views import RegisterView

app_name = 'accounts'

urlpatterns = [
    path('register_new/', RegisterView.as_view(), name='auth_register'),
]
