from django.contrib import admin
from django.urls import path, include

from account.views import login_view,register_view,logout_view

app_name = 'account'

urlpatterns = [
    path('', login_view, name='login_view'),
    path('register/', register_view , name='register'),    
    path('logout/', logout_view, name='logout_view'),
]
