from django.contrib import admin
from django.urls import path
from inicio import views
from registros import views as views_registros
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rutas de la App Registros (Datos de DB)
    path('', views_registros.registros, name="Principal"),
    path('registrar/', views_registros.registrar, name="Registrar"),
    path('consultarComentario/', views_registros.consultarComentarioContacto, name="Comentarios"),
    path('eliminarComentario/<int:id>/', views_registros.eliminarComentarioContacto, name="Eliminar"),
    path('contacto/', views.contacto, name="Contacto"),
    path('formulario/', views.formulario, name="Formulario"),
    path('comentario/editar/<int:id>/', views_registros.editarComentarioContacto, name="Editar"),
    path('seguridad/', views_registros.seguridad, name="Seguridad"),
    
    # Rutas para las distintas consultas a la BD
    path('consultas1/', views_registros.consultar1, name="Consulta1"),
    path('consultas2/', views_registros.consultar2, name="Consulta2"),
    path('consultas3/', views_registros.consultar3, name="Consulta3"),
    path('consultas4/', views_registros.consultar4, name="Consulta4"),
    path('consultas5/', views_registros.consultar5, name="Consulta5"),
    path('consultas6/', views_registros.consultar6, name="Consulta6"),
    path('consultas7/', views_registros.consultar7, name="Consulta7"),
    path('consultasSQL/', views_registros.consultasSQL, name="Sql"),
]

# Servir archivos media en entorno de desarrollo
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)