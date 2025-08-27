from django.http import HttpResponse
from django.shortcuts import render
from .models import Contactos


def test(request):
    return render(request, 'hola.html')

def pagina(request):
    if request.method == 'POST':
        Contactos.objects.create(nombre=request.POST['nombre'], 
                                apellido=request.POST['apellido'], 
                                email=request.POST['email'], 
                                motivo=request.POST['motivo'])
        return render(request, 'IndexUS.html')
    else:    
        return render(request, 'IndexUS.html')

#Pagina del Juan
def PaginaJuan(request):
    return render(request, 'Juan.html')

#Pagina del Roberto
def PaginaRoberto(request):
    return render(request, 'Roberto.html')

