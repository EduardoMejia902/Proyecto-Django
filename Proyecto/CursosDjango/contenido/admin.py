from django.contrib import admin
from .models import Curso, Actividad

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('clave', 'curso', 'fecha_creacion')
    search_fields = ('clave', 'curso__nombre')
    date_hierarchy = 'fecha_creacion'
    list_filter = ('curso',)

admin.site.register(Curso)
admin.site.register(Actividad, ActividadAdmin)