from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path("",csrf_exempt(CompanyOperation.as_view())),
    path("/<int:id>",csrf_exempt(CompanyIdOperation.as_view()))
]
