from django import forms
from .models import Perfiles

class SignupForm(forms.ModelForm):
    class Meta:
        model = Perfiles
        fields = ['nombre', 'mail', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }