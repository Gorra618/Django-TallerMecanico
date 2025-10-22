from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('services/', views.services, name='services'),
    path('budget/', views.budget, name='budget'),
    path('cotization/', views.cotization, name='cotization'),
]