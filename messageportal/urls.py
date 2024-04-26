from django.urls import path
from messageportal.views import index 

app_name = 'messageportal'

urlpatterns = [
    path('messageportal/', index, name='index')
]
