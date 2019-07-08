from django.urls import path
from .views import index, en, pl

urlpatterns = [
    path('', index, name="index"),
    path('en/', en, name="en"),
    path('pl/', pl, name="pl")
]