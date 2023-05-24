from django.urls import path
from .views import *

urlpatterns = [
    path("",csrf_exempt(UserOperation.as_view()))
]
