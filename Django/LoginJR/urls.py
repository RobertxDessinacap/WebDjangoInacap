from django.urls import path

from .views import LoginJR, testlogin, mostrardatos, hacerlogout, borrardatos, borrarJuan, borrarRoberto

urlpatterns = [
    path('salir/', hacerlogout),
    path('', LoginJR),
    path('test/', testlogin),
    path('visual/', mostrardatos, name='visual'),
    path('borrar/<int:id>/', borrardatos, name='borrar'),
    path('borrarJuan/<int:id>/', borrarJuan, name='borrarJuan'),
    path('borrarRoberto/<int:id>/', borrarRoberto, name='borrarRoberto')    
]