from django.urls import path
from . import views # import views from current directory

urlpatterns = [
    path("", views.index, name="index"),
    path("andrew", views.andrew, name="andrew") # the index function I created in views.py
]
