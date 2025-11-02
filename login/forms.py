from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa tu contraseña'}),
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Repite la contraseña'}),
    )

    class Meta:
        model = Usuario
        fields = ['username', 'nombre_completo', 'email', 'rol']
        labels = {
            'username': 'Nombre de usuario',
            'nombre_completo': 'Nombre completo',
            'email': 'Correo electrónico',
            'rol': 'Rol',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Usuario'}),
            'nombre_completo': forms.TextInput(attrs={'placeholder': 'Tu nombre completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.cl'}),
            'rol': forms.Select(attrs={'class': 'form-select'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False  # Queda pendiente de aprobación del admin
        if commit:
            user.save()
        return user