from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from JR.models import Contactos, JuanContacto, RobertoContacto
# Create your views here.


@login_required
def testlogin(request):
    if request.method == 'GET':
        return render(request, 'testlogin.html', {
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #crear usuario
            try:
                user=User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('visual')
            except:
                return render(request, 'testlogin.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        else:
            return render(request, 'testlogin.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden'
            })
    
#Hacer LOGOUT
def hacerlogout(request):
    logout(request)
    return redirect('/privado')


#Hacer login
def LoginJR(request):
    if request.method == 'GET':
        print("GET")
        return render(request, 'login.html')
    else:
        print(request.POST)
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'login.html', {
                'error': 'El usuario o la contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('visual')

@login_required
def mostrardatos(request):
    contactos = Contactos.objects.all()
    juanContacto = JuanContacto.objects.all()
    robertoContacto = RobertoContacto.objects.all()

    return render(request, 'visualDB.html', {
        'infocontactos': contactos,
        'JuanContactos': juanContacto,
        'RobertoContactos': robertoContacto
    })


@login_required
def borrardatos(request, id):
    contacto = get_object_or_404(Contactos, id=id)
    contacto.delete()
    return redirect('visual')

@login_required
def borrarJuan(request, id):
    contacto = get_object_or_404(JuanContacto, id=id)
    contacto.delete()
    return redirect('visual')

@login_required
def borrarRoberto(request, id):
    contacto = get_object_or_404(RobertoContacto, id=id)
    contacto.delete()
    return redirect('visual')