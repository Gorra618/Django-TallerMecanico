from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'main.html')

def services(request):
    return render(request, 'services.html')

def budget(request):
    return render(request, 'budget.html')

def cotization(request):
    return render(request, 'cotization.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')