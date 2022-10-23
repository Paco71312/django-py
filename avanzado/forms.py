from django import forms
class MascotaFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    tipo=forms.CharField(max_length=30)
    edad=forms.IntegerField()
    fecha_nacimiento=forms.DateField()
    
class BusquedaMascota(forms.Form):
    nombre= forms.CharField(max_length=30)