from django.urls import path
from . import views
from .views import signup_view, login_view

urlpatterns = [
    path('', views.main, name='main'),
    path('services/', views.services, name='services'),
    path('budget/', views.budget, name='budget'),
    path('cotization/', views.cotization, name='cotization'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
        path('signup/', signup_view, name='signup'),

]
