from django.urls import path

from .views import LoginJR, testlogin, mostrardatos, hacerlogout

urlpatterns = [
    path('salir/', hacerlogout),
    path('', LoginJR),
    path('test/', testlogin),
    path('visual/', mostrardatos, name='visual')
    
]