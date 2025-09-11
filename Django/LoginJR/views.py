from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from hashlib import sha256


# Create your views here.
def LoginJR(request):
    return render(request, 'login.html')


def testlogin(request):

    return render(request, 'testlogin.html', {
        'form': UserCreationForm
    })

def mostrardatos(request):
    return render(request, 'visualDB.html')