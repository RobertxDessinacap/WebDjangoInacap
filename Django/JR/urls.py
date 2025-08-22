from django.urls import path

from . import views

urlpatterns = [
    
    path('testeo/', views.test),
    path('', views.pagina),
    path('Juan/', views.PaginaJuan),
    path('Roberto/', views.PaginaRoberto)
]