from django.urls import path
from . import views

urlpatterns = [
    path("", views.help, name="help"),
    path("help/", views.help, name="help")
]
