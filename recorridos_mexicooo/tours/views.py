from django.shortcuts import render,get_object_or_404
from .models import Tours
from datetime import date

# Create your views here.
def tours(request):
    hoy = date.today()
    tours = Tours.objects.filter(fecha__gt=hoy)
    return render(request,"tours/tours.html",{"tours":tours})

def catalogos(request):
    return render(request,"tours/catalogos.html")

def mich(request):
    hoy = date.today()
    tours = Tours.objects.filter(estado="Michoacán", fecha__gt=hoy)
    return render(request,"tours/estados/michoacan/mich.html",{"tours":tours})

def qro(request):
    hoy = date.today()
    tours = Tours.objects.filter(estado="Querétaro", fecha__gt=hoy)
    return render(request,"tours/estados/queretaro/qro.html",{"tours":tours})

def realizados(request):
    hoy = date.today()
    tours = Tours.objects.filter(fecha__lt=hoy)
    return render(request,"tours/realizados.html",{"tours":tours})

def detalle_tour(request, id):
    tours = get_object_or_404(Tours, pk=id)
    return render(request, 'tours/detalles.html', {'tours': tours})
