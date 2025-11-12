from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import logout
from .models import Presupuesto, Cotizacion, Perfiles
from .forms import SignupForm
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'main.html')

def services(request):
    return render(request, 'services.html')

def budget(request):
    presupuesto = Presupuesto.objects.first()  # Asume que hay un único presupuesto
    return render(request, 'budget.html', {'presupuesto': presupuesto})

def cotization(request):
    cotizaciones = Cotizacion.objects.all()
    return render(request, 'cotization.html', {'cotizaciones': cotizaciones})


def login_view(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        contraseña = request.POST.get('contraseña')
        try:
            perfil = Perfiles.objects.get(mail=mail, contraseña=contraseña)
            return redirect('main')  # Redirige al inicio si las credenciales son correctas
        except Perfiles.DoesNotExist:
            error = "Correo o contraseña incorrectos"
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al inicio de sesión después del registro
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('main')  # Redirige al inicio de sesión después de cerrar sesión

@login_required
def protected_view(request):
    # Lógica de la vista
    pass