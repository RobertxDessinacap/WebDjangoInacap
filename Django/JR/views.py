from django.http import HttpResponse
from django.shortcuts import render



def test(request):
    return render(request, 'hola.html')

def pagina(request):
    return render(request, 'index.html')

#Vagina del Juan
def PaginaJuan(request):
    return render(request, 'Juan.html')

#Pagina del Roberto
def PaginaRoberto(request):
    return render(request, 'Roberto.html')

