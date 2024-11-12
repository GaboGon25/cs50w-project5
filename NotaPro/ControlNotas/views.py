from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth .decorators import login_required

from .models import User



# Create your views here.
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            print("Usuario autenticado correctamente")  # Mensaje de depuración
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            print("Fallo en la autenticación")  # Mensaje de depuración
            return render(request, "ConrtrolNotas/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, 'ControlNotas/login.html')

def register(request):
     if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "ControlNotas/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "ControlNotas/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
     else:
         return render(request, 'ControlNotas/register.html')
     
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def index(request):
     return render(request, 'ControlNotas/index.html')

def create_semester(request):
     return render(request, 'ControlNotas/registro_semestre.html')

def create_classes(request):
     return render(request, 'ControlNotas/registro_clase.html')

def classes(request):
     return render(request, 'ControlNotas/clase.html')

def partial(request):
     return render(request, 'ControlNotas/parcial.html')

def create_evaluation(request):
     return render(request, 'ControlNotas/crear_evaluacion.html')

def all_evaluation(request):
     return render(request, 'ControlNotas/ver_evaluacion.html')
     
def evaluation_detail(request):
     return render(request, 'ControlNotas/detalle_evaluacion.html')
     
     
     