from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login as login_auth,logout
from django.contrib.auth.models import User # Extraer el modelo de usuarios DJANGO 
from django.contrib import messages
from usuarios.models import Usuarios
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.utils import timezone

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def principal(request):
    return render(request,"inicio/principal.html")

def nosotros(request):
    return render(request,"inicio/nosotros.html")

def catalogos(request):
    return render(request,"inicio/catalogos.html")

def favoritos(request):
    return render(request,"inicio/favoritos.html")

# def sesion(request):
#     return render(request,"inicio/sesion.html")

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #Saving form user data in the model
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login_auth(request, user)#Autenticar usuario automaticamente
                return redirect('principal')  # Redirigir a la página principal
        else:
            print(form.errors)  # mostrar los errores en la consola
            
    else:
        form = UserCreationForm()
    return render(request,"inicio/cuenta/registro.html",{"form":form})

def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['contraseña']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_auth(request, user)
            return redirect('principal')  # Redirige a la página principal o donde quieras
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos.'
            return render(request, 'inicio/cuenta/login.html', {'error_message': error_message})
    return render(request, 'inicio/cuenta/login.html')

@login_required
def cuenta(request):
    usuario = request.user #obtiene el usuario que esta en sesion
    """ if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user.perfil)
        if form.is_valid():
            form.save()
            return redirect('cuenta')
    else:
        form = PerfilForm(instance=request.user.perfil) """
    return render(request, 'inicio/cuenta/salir.html',{"usuario":usuario})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('principal')


