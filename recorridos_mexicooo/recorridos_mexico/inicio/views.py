from django.shortcuts import render, HttpResponse


# Create your views here.

def principal(request):
    return render(request,"inicio/principal.html")

def nosotros(request):
    return render(request,"inicio/nosotros.html")

def catalogos(request):
    return render(request,"inicio/catalogos.html")

def favoritos(request):
    return render(request,"inicio/favoritos.html")

def sesion(request):
    return render(request,"inicio/sesion.html")

def registro(request):
    return render(request,"inicio/registro.html")
