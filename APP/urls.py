from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('services/', views.services, name='services'),
    path('budget/', views.budget, name='budget'),
    path('cotization/', views.cotization, name='cotization'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]