from itertools import product
from django.shortcuts import render
from django.shortcuts import redirect # importacion para redirigir a una pagina 

from django.contrib import messages #para enviar mensajes del servidor al cliente
from django.contrib.auth import authenticate  # linea de codigo para autenticar a un usuario!!
from django.contrib.auth import login # importacion para loguear a un usuario
from django.contrib.auth import logout # importacion para salir de la sesion donde estas logueado

from django.contrib.auth.models import User

from products.models import Products # para crear nuevos usuarios

from .forms import RegisterForm # para registrar a un usuario (formulario de django)

from products.models import Products



def index(request):

    products = Products.objects.all().order_by('-id')

    return render(request,'index.html',{
        'message': 'Lista de productos',
        'title': 'productos',
        'products': products,
        
    })

def login_view(request): # funcion para logear y autenticar usuarios
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username =request.POST.get('username') #diccionario
        password =request.POST.get('password')

        user =  authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')# funcion para redirigir a la pagina principal
        else:
            messages.error(request, 'Usuario o Contraseña no validos')
    return render(request, 'users/login.html', {

    })

def logout_view(request): # funcion para salir exitosamente o desloguear

    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')

def register(request):# para crear nuevos usuarisos
    if request.user.is_authenticated:
        return redirect('index')
    
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index') 

    return render(request, 'users/register.html', {
        'form': form
    })