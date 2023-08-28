from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DeporteForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre", required=True)
    categoría = forms.CharField(max_length=50, label="Categoría", required=True)
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche"),
    )

    turno = forms.ChoiceField(label="Turno elegido", choices=TURNOS, required=True)

class DeportistaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField()
    edad = forms.IntegerField()
    federado = forms.BooleanField(required=False)

class EntrenadorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField()
    fechaAlta = forms.DateField(label="Fecha de Alta")

class ClubForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    domicilio = forms.CharField(max_length=50, required=True)
    teléfono = forms.CharField(max_length=50, required=True)

class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)
