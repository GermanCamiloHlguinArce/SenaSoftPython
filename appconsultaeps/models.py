from django.db import models
from django.contrib.auth.models import AbstractUser, User


class tipo_doc (models.Model):
    doc=models.CharField(max_length=20, null=False,blank=False)


class pacientes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    edad=models.PositiveIntegerField()
    peso=models.PositiveIntegerField()
    estatura=models.PositiveIntegerField()
    estado_civil=models.CharField(max_length=45, null=False,blank=False)
    tipo_doc=models.ForeignKey(tipo_doc, on_delete=models.CASCADE)
