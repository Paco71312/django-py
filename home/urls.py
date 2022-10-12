from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hola/', views.hola, name='hola'),
    path('otra-vista/', views.otra_vista),
    path('fecha/', views.fecha,name='fecha'),
    #cuando yo quiero pasar parametros  lo pongo entre corchetes
    path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento),
    #para importar templates
    path('mi-template/', views.mi_template, name='mi_template'),
    #clase2 Agregando un parametro de nombre 
    path('prueba-template/', views.prueba_template),
    path('ver_personas/', views.ver_personas, name='ver_personas'),
    path('crear_persona/', views.crear_persona, name='crear_persona'), 
    
    ]