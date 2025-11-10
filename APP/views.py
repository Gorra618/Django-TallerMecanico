from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import logout

def main(request):
    return render(request, 'main.html')

def services(request):
    return render(request, 'services.html')

def budget(request):
    return render(request, 'budget.html')

def cotization(request):
    return render(request, 'cotization.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect('main')
        else:
            messages.error(request, "Credenciales inválidas.")
            return redirect('login')
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe.")
            return render(request, "signup.html")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Cuenta creada con éxito. Ahora puedes iniciar sesión.")
        return redirect("login")

    return render(request, "signup.html")

def logout_view(request):
    logout(request)
    return redirect('login')