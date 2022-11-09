#creacion de formularios para registrar 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # basado en user creation form 
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class MiFormularioDeCreacion(UserCreationForm):
    username= forms.CharField(label= 'Usuario' ,max_length=20)
    password1=forms.CharField(label='Contraseña:',  widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir Contraseña:',widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={key:'' for key in fields}
        
        
class EditarPerfilFormulario(forms.Form):
    
    first_name=forms.CharField(label= 'Nombre')
    last_name=forms.CharField(label= 'Apellido')
    email=forms.CharField()
    avatar=forms.ImageField(required=False)
    
class MiCambioDePassword(PasswordChangeForm):
    old_password=forms.CharField(label='Contraseña Anterior:',  widget=forms.PasswordInput)
    new_password1=forms.CharField(label='Nueva Contraseña:',widget=forms.PasswordInput)
    new_password2=forms.CharField(label='Repetir Contraseña:',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['old_password','new_password1','new_password2']
        help_texts={key:'' for key in fields}