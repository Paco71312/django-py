from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# creacion de avatar 
class ExtesionUsuario(models.Model):
    #avatar=imagen 
    avatar=models.ImageField(upload_to='avatares',null=True, blank=True)
    #como se relacion aco ele usuario 
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.CASCADE)