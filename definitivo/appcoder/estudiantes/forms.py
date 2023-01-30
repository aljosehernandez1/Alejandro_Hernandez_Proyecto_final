from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from estudiantes.models import Avatar


class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    comision = forms.IntegerField(required=True, max_value=2000)
    duracion = forms.IntegerField()
    descripcion = forms.CharField(max_length=1000)


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']
        
class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']