#creacion de vistas, se definene como una clase 
from importlib.abc import Loader
from re import template
from django.http import HttpResponse
from datetime import datetime, timedelta
#para importar tu template
from django.template import Context,Template,loader
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
#simplificando un poco el template y eso es importando loader
