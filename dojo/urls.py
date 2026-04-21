from django.urls import path
from .views import dojo_view

urlpatterns = [
    path("", dojo_view, name="dojo")
]