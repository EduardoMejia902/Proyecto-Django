from django.contrib import admin
from django.urls import path
from contenido import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="Principal"),
    path('cursos/', views.cursos, name="Cursos"),
    path('contacto/', views.contacto, name="Contacto"),
]