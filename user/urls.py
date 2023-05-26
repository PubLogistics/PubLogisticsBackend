from django.urls import path
from .views import *
from django.contrib.auth.views import  LoginView


urlpatterns = [
    path("/login/",LoginView.as_view()),
    path("",csrf_exempt(UserOperation.as_view()))
]
