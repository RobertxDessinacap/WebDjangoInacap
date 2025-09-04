from django.urls import path

from .views import LoginJR

urlpatterns = [
    path('', LoginJR)
]