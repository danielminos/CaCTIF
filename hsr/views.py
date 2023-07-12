from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
from serviciosmedicos.models import Servicios,Profesionales,Atencion

def saludo(request):
    return render(request,"index.html")

def contacto(request):
    return render(request,"contacto.html")

def institucional(request):
    director_a="RODRIGUEZ SICILIANO VERONICA"
    Stecnico="SOSA SILVIO"
    return render(request,"institucional.html",{"nombre_directora":director_a},{"nombre_sectecnico":Stecnico})

def licitaciones(request):
    return render(request,"licitaciones.html")

def pacientes(request):
    return render(request,"pacientes.html")

def servicios(request):
    servicios=Servicios.objects.all()
    profesionales=Profesionales.objects.all()
    atenciones=Atencion.objects.all()
    return render(request,"serviciosmedicos.html",{"servicios":servicios,"profesionales":profesionales,"atenciones":atenciones})
