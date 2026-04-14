from django.shortcuts import render

def contacto(request):
    return render(request, "registros/contacto.html")

def formulario(request):
    return render(request, "inicio/formulario.html")