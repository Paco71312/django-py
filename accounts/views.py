
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from accounts.forms import MiFormularioDeCreacion
# Create your views here.

def mi_login(request):
    if request.method== 'POST':
        formulario= AuthenticationForm(request,data=request.POST)
        if formulario.is_valid():
            usuario= formulario.get_user() #permite que se loege
            login(request,usuario)
            return redirect('index')
    else:
        formulario=AuthenticationForm()
    return render(request, 'accounts/login.html',{'formulario':formulario})

#  Por meto de Django directo 
# def registrar(request):
#     if request.method== 'POST':
#         formulario=UserCreationForm(request.POST)
#         if formulario.is_valid():
#             #creacion de usuario
#             formulario.save() #nos permite crear un usuario nuevo
#             return redirect('index')
#     else:
#         formulario=UserCreationForm()        
#     return render(request, 'accounts/registrar.html',{'formulario':formulario})

def registrar(request):
    if request.method== 'POST':
        formulario=MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            #creacion de usuario
            formulario.save() #nos permite crear un usuario nuevo
            return redirect('index')
    else:
        formulario=MiFormularioDeCreacion()        
    return render(request, 'accounts/registrar.html',{'formulario':formulario})