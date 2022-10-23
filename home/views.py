#creacion de vistas, se definene como una clase 
from importlib.abc import Loader
from re import template
from django.http import HttpResponse
from datetime import datetime, timedelta
#para importar tu template
from django.template import Context,Template,loader
#Clase 3
from django.shortcuts import render, redirect
#clase 3
import random

from home.forms import HumanoFormulario,BusquedaHumano
from home.models import Humano
def hola(request):
    
    return HttpResponse('<h1>Hola clase</h1>')
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
    cargar_archivo=open(r'C:\Users\Sistemas\Desktop\django\proyecto-clases\home\templates\home\mi_template.html', 'r')
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
    template=loader.get_template('home/tu_template.html')
    renderizar_template=template.render({'persona':nombre})
    return HttpResponse(renderizar_template)
#simplificando un poco el template y esoes importando loader

def prueba_template(request):

    #mostrar los numero del 1 al 10 
    mi_contexto={'rango':list(range(1,11)),
                 'valor_aleatorio':random.randrange(1,11)}
        
    template=loader.get_template('home/prueba_template.html')
    renderizar_template=template.render(mi_contexto)
    return HttpResponse(renderizar_template)
# crear  la vista para el  modelo 
def crear_persona(request):
    #print(request.method) Para ver que metodo ocuapara
    #print(request.GET) Para veri que querry te esta dando 
    #print(request.POST) #Para ver que querry te esta dando  
    if request.method=='POST':
        formulario=HumanoFormulario(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data #informacion limpia 
            nombre=data['nombre']
            apellido=data['apellido']
            edad=data['edad']
            fecha_creacion=data['fecha_creacion']
            if not fecha_creacion:
                fecha_creacion=datetime.now()
            #v2    
            #fecha_creacion=data['fecha_creacion'] or datetime.now()
        
            persona=Humano(nombre=nombre,apellido=apellido,edad=edad,fecha_creacion=fecha_creacion)
            persona.save()
            
        
        return redirect('ver_personas') #nombre que esta en el archvio de url
    formulario=HumanoFormulario()
    return render(request,'home/crear_persona.html',{'formulario':formulario})
   



def ver_personas(request):
    nombre=request.GET.get('nombre',None)
    if nombre:
        persona= Humano.objects.filter(nombre__icontains=nombre)
    else:
        persona=Humano.objects.all()
    formulario=BusquedaHumano()
    return render(request,'home/ver_personas.html',{'personas':persona, 'formulario':formulario})
    # template=loader.get_template('ver_personas.html')
    # renderizar_template=template.render({'personas':persona})
    # return HttpResponse(renderizar_template)  
    
def index(request):
    return render(request,'home/index.html')
    