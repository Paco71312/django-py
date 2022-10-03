#creacion de vistas, se definene como una clase 
from importlib.abc import Loader
from re import template
from django.http import HttpResponse
from datetime import datetime, timedelta
#para importar tu template
from django.template import Context,Template,loader
import random

from home.models import Persona
def hola(request):
    return HttpResponse("Buenas clase 41765!")

def otra_vista(request):
    return HttpResponse("<h1>Escrito con html</h1>") 

def fecha(request):
    fecha_y_hora = datetime.now()
    return  HttpResponse(f'La fecha y hora actual es {fecha_y_hora}')
#pasaje de parematros en este caso edad 
def calcular_fecha_nacimiento(request, edad):
    fecha= datetime.now().year - edad
    return HttpResponse(f'Tu año aproximada para tus {edad} años seria: {fecha}')
#importacion de templates
def mi_template(request):
    #Clase 1: como se hacia antes 
    cargar_archivo=open(r'C:\Users\Sistemas\Desktop\django\proyecto-clases\templates\mi_template.html', 'r')
    crear_template=Template(cargar_archivo.read())
    cargar_archivo.close
    #puesta en marcha 
    contexto = Context()
    renderizar_template = crear_template.render(contexto)
    return HttpResponse(renderizar_template)

# clase 2 de Django 
def tu_template(request,nombre):
    #COMO ANTES SE HACIA
    # cargar_archivo=open(r'C:\Users\Sistemas\Desktop\django\proyecto-clases\templates\tu_template.html', 'r')
    # crear_template=Template(cargar_archivo.read())
    # cargar_archivo.close
    # #puesta en marcha 
    # contexto = Context({'persona':nombre})#contine la informacion que nosotros le queremsoo pasar al templete
    # renderizar_template = crear_template.render(contexto) 
    
    #CON LOADER
    template=loader.get_template('tu_template.html')
    renderizar_template=template.render({'persona':nombre})
    return HttpResponse(renderizar_template)
#simplificando un poco el template y esoes importando loader

def prueba_template(request):

    #mostrar los numero del 1 al 10 
    mi_contexto={'rango':list(range(1,11)),
                 'valor_aleatorio':random.randrange(1,11)}
        
    template=loader.get_template('prueba_template.html')
    renderizar_template=template.render(mi_contexto)
    return HttpResponse(renderizar_template)
# crear  la vista para el  modelo 
def crear_persona(request,nombre,apellido):
    persona=Persona(nombre=nombre,apellido=apellido,edad=random.randrange(1,99),fecha_nacimiento=datetime.now())
    persona.save()
    template=loader.get_template('crear_persona.html')
    renderizar_template=template.render({'persona':persona})
    return HttpResponse(renderizar_template)



def ver_personas(request):
    # con esto se tra todos lo aobjetos de persona que tiene el modelo 
    personas=Persona.objects.all
    template=loader.get_template('ver_personas.html')
    renderizar_template=template.render({'personas':personas})
    return HttpResponse(renderizar_template)  
    
