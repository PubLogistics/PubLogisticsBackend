from django.urls import path
from .views import *

urlpatterns = [
    path("/register",csrf_exempt(Register.as_view())),
    path("/login",csrf_exempt(Login.as_view()))
]
