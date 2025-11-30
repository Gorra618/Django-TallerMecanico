from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Presupuesto, Cotizacion, Perfiles
from .forms import SignupForm
from django.contrib.auth.decorators import login_required

def main_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'main.html')

def services(request):
    return render(request, 'services.html')

def budget(request):
    presupuesto = Presupuesto.objects.first() 
    return render(request, 'budget.html', {'presupuesto': presupuesto})

def cotization(request):
    cotizaciones = Cotizacion.objects.all()
    return render(request, 'cotization.html', {'cotizaciones': cotizaciones})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        if not username or not password:
            messages.error(request, 'Por favor, completa todos los campos.')
            return render(request, 'login.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')  

@login_required
def protected_view(request):
    pass