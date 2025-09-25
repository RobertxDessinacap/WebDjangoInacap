from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contactos, RobertoContacto, JuanContacto



def pagina(request):
    if request.method == 'POST':
        Contactos.objects.create(nombre=request.POST['nombre'], 
                                apellido=request.POST['apellido'], 
                                email=request.POST['email'], 
                                motivo=request.POST['motivo'])
        return redirect('/')
    else:    
        return render(request, 'IndexUS.html')

#Pagina del Juan
def PaginaJuan(request):
    if request.method == 'POST':
        JuanContacto.objects.create(nombre=request.POST['nombre'],
                                    apellido=request.POST['apellido'],
                                    telefono=request.POST['telefono'],
                                    email=request.POST['email'],
                                    mensaje=request.POST['mensaje'])
        return redirect('/Juan/')
    else:
        return render(request, 'Juan.html')

#Pagina del Roberto
def PaginaRoberto(request):
    if request.method == 'POST':
        RobertoContacto.objects.create(nombre=request.POST['nombreDB'], 
                                apellido=request.POST['apellidoDB'], 
                                correo=request.POST['emailDB'], 
                                motivo=request.POST['motivoDB'])
        return redirect('/Roberto/')
    else:    
        return render(request, 'Roberto.html')