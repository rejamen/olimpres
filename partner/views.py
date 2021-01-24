"""Core views for devices app."""
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Partner
from .forms import CreateUserForm

@login_required
def home(request):
    """Partner dashboard."""
    user = request.user
    partner = Partner.objects.get(user=user)
    data = {
        'partner': partner,
    }
    template = 'partner/home.html'
    return render(request, template, data)

def request_logout(request):
    """User logout."""
    logout(request)
    return redirect('partner:home')

def register(request):
    """Partner register."""
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request,
                'Usuario {} registrado con éxito'.format(user)
            )
            return redirect('base:index')
    data = {'form': form}
    template = 'partner/register.html'
    return render(request, template, data)
