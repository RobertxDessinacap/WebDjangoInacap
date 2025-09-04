from django.shortcuts import render
from hashlib import sha256

# Create your views here.
def LoginJR(request):
    return render(request, 'login.html')