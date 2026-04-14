from django.shortcuts import render
from .models import Curso

def principal(request):
    # Página principal con mensaje de bienvenida
    return render(request, "contenido/principal.html")

def cursos(request):
    # Mostrar la lista de cursos disponibles en BD
    lista_cursos = Curso.objects.all()
    return render(request, "contenido/cursos.html", {'cursos': lista_cursos})

def contacto(request):
    # Mostrar el formulario
    cursos_disponibles = Curso.objects.all()
    return render(request, "contenido/contacto.html", {'cursos': cursos_disponibles})