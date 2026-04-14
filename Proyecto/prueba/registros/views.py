from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumnos, ComentarioContacto
from .forms import ComentarioContactoForm

def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            # Usamos redirect para seguir el patrón Post/Redirect/Get
            return redirect('Comentarios')
    else:
        form = ComentarioContactoForm()
    return render(request, 'registros/contacto.html', {'form': form})

def consultarComentarioContacto(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        return redirect('Comentarios')
    return render(request, confirmacion, {'object': comentario})

# La vista consultarComentarioIndividual se ha fusionado con editarComentarioContacto
# para seguir mejores prácticas.

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('Comentarios')
    else: # Manejo de GET
        form = ComentarioContactoForm(instance=comentario)
    return render(request, 'registros/formEditarComentario.html', {'form': form, 'comentario': comentario})

def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar2(request):
    alumnos = Alumnos.objects.filter(carrera="TI", turno="Matutino")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar3(request):
    alumnos = Alumnos.objects.all().only('matricula', 'nombre', 'carrera', 'turno', 'imagen')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar4(request):
    alumnos = Alumnos.objects.filter(turno__contains="Vesp")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar5(request):
    alumnos = Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar6(request):
    alumnos = Alumnos.objects.filter(created__range=('2021-07-01', '2021-07-13'))
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar7(request):
    alumnos = Alumnos.objects.filter(comentario__coment__contains='No Inscrito')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultasSQL(request):
    alumnos = Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request, "registros/seguridad.html", {'nombre': nombre})
