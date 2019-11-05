from django.db import models
from django.core.validators import MinValueValidator
import re
from django.core.validators import RegexValidator
# Create your models here.

class Sistema(models.Model):
    TYPE_CHOICES = (('mysql', 'Mysql'),
                   ('postgresql', 'PostgreSQL'))
    FREQUENCY_CHOICES = (('days', 'Days'),
                   ('hours', 'Hours'),
                   ('minutes', 'Minutes'), 
                   ('seconds', 'Seconds'))
    id_system=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    bd_name=models.CharField(max_length=200)
    bd_type= models.CharField(max_length=11, choices=TYPE_CHOICES)
    frequency=models.IntegerField(validators=[MinValueValidator(1)])
    type_frequency=models.CharField(max_length=11, choices=FREQUENCY_CHOICES)
    server_ip=models.CharField(max_length=20,validators=[RegexValidator((re.compile('([0-9]{1,3}.?){4}')), ('ip incorrecta'), 'invalid')])
    server_username=models.CharField(max_length=200)
    server_password=models.CharField(max_length=200)
    server_route_save=models.CharField(max_length=500, blank=True, null=True)
    copy_to_server=models.BooleanField(blank=True, default=False)
    copy_to_drive=models.BooleanField(blank=True, default=False)
    def __str__(self):    
        '''Devuelve el modelo en tipo String'''
        return str(self.name)

class CopiaRespaldo(models.Model):
    TYPE_CHOICES = (('drive', 'Drive'),
                   ('server', 'Server'))
    id_respaldo=models.AutoField(primary_key=True)
    id_system=models.ForeignKey(Sistema, on_delete=models.CASCADE)
    receptor_server_username=models.CharField(max_length=200)
    receptor_password=models.CharField(max_length=200, default="password")
    receptor_server_ip=models.CharField(max_length=20,validators=[RegexValidator((re.compile('([0-9]{1,3}.?){4}')), ('ip incorrecta'), 'invalid')])
    receptor_route_save=models.CharField(max_length=500)   
    receptor_type= models.CharField(max_length=11, choices=TYPE_CHOICES, default="server") 
    
    def __str__(self):    
        '''Devuelve el modelo en tipo String'''
        return str(self.id_respaldo)