from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render


def index(request):
    """Home page."""
    template = 'base/index.html'
    data = {
        'error': False,
        'logout': False,
    }
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(
                request,
                'El usuario especificado no existe.'
            )
            return render(request, template, data)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('partner:home')
        else:
            messages.error(
                request,
                'Usuario o contraseña incorrectos'
            )
            return render(request, template, data)
    return render(request, template, data)
