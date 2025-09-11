from django.urls import path

from .views import LoginJR, testlogin, mostrardatos

urlpatterns = [
    path('', LoginJR),
    path('/test/', testlogin),
    path('/visual/', mostrardatos)
]