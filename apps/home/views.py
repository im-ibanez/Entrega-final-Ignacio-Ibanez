from django.shortcuts import render, redirect, HttpResponse
from django import forms
# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

#Decorador por defecto
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")

@login_required
def inicio(request):
    return render(request, "home/index.html")


def logout_request(request):
    logout(request)
    messages.info(request, "Saliste sin problemas")
    return redirect("inicio")
     

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasena)
            if user is not None:
                login(request, user)
                return render(request,"home/index.html",  {"mensaje":f"Bienvenido {usuario}"} )
            else:
                return render(request,"home/login.html", {"mensaje":"Error, datos incorrectos"} )
        else:                        
            return render(request,"home/login.html" ,  {"mensaje":"Error, formulario erroneo"})
    form = AuthenticationForm()
    return render(request,"home/login.html", {'form':form} )



def register(request):
    if request.method == 'POST':
#form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"home/index.html" ,  {"mensaje":"Usuario Creado :)"})
        else:
            #form = UserCreationForm()       
            form = UserRegisterForm()
            return render(request, "home/registro.html", {"form": form})
    else:
        form = UserRegisterForm()
        return render(request, "home/registro.html", {"form": form})   