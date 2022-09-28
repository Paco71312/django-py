#creacion de vistas, se definene como una clase 
from re import template
from django.http import HttpResponse
from datetime import datetime, timedelta
#para importar tu template
from django.template import Context,Template
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
    cargar_archivo=open(r'C:\Users\Sistemas\Desktop\django\proyecto-clases\templates\template.html', 'r')
    crear_template=Template(cargar_archivo.read())
    cargar_archivo.close
    #puesta en marcha 
    contexto = Context()
    renderizar_template = crear_template.render(contexto)
    return HttpResponse(renderizar_template)
