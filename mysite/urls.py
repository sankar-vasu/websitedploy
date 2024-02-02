from django.urls import path
from .views import myName

urlpatterns =[
    path("m",myName,name="display"),
]