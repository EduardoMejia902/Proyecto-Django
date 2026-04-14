from django.db import models
from ckeditor.fields import RichTextField

# Modelo Cursos (necesario para la relación)
class Curso(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Curso")
    categoria = models.CharField(max_length=100, help_text="Ej: Base de datos, Programación, etc.")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre

# Modelo Actividad (Solicitado en la Actividad de la Parte 4)
class Actividad(models.Model):
    clave = models.CharField(max_length=50, unique=True, verbose_name="Clave de la Actividad")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nombre del Curso")
    descripcion = RichTextField(verbose_name="Descripción de la actividad")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.clave} - {self.curso.nombre}"