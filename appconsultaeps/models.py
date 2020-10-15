from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from datetime import datetime


class tipo_doc(models.Model):
    doc=models.CharField(max_length=20, null=False,blank=False)

    def __str__(self):
        return self.doc

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documento'

class especialista(models.Model):
    especialidad=models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.especialidad

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'


class medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='medico')
    numero_doc=models.PositiveIntegerField()
    telefono=models.PositiveIntegerField()
    tipo_doc = models.ForeignKey(tipo_doc, on_delete=models.CASCADE)
    especialista=models.ForeignKey(especialista,on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} {}'.format(self.numero_doc, self.user.first_name, self.user.last_name)


    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'
        

class pacientes(models.Model):
    num_doc = models.PositiveIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='paciente')
    edad=models.PositiveIntegerField()
    peso=models.PositiveIntegerField()
    estatura=models.PositiveIntegerField()
    estado_civil=models.CharField(max_length=45, null=False,blank=False)
    tipo_doc=models.ForeignKey(tipo_doc, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} {}'.format(self.num_doc, self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class grupo_familiar(models.Model):
    paciente = models.ForeignKey(pacientes, on_delete=models.CASCADE)
    paciente_titular =  models.IntegerField(null=True, blank=True)
    medico=models.ForeignKey(medico,on_delete=models.CASCADE)

    def __str__(self):
        return self.medico

    
    class Meta:
        verbose_name = 'Grupo de familia'
        verbose_name_plural = 'Grupos de familias'



class historia_clinica(models.Model):
    incapacidad=models.CharField(max_length=50,null=True,blank=True)
    pacientes=models.ForeignKey(pacientes,on_delete=models.CASCADE)
    motivo_consulta=models.TextField(max_length=150,null=False,blank=False)
    enfermedades_actual=models.CharField(max_length=150,null=False,blank=False)
    antecedentes=models.CharField(max_length=150,null=False,blank=False)
    analisis=models.CharField(max_length=150,null=False,blank=False)
    plan_manejo=models.CharField(max_length=150,null=False,blank=False)

    def __str__(self):
        return self.pacientes.user.first_name

    class Meta:
        verbose_name = 'Historial clinico'
        verbose_name_plural = 'Historias clinicas'


class citas(models.Model):
    fecha=models.DateField()
    pacientes=models.ForeignKey(pacientes,on_delete=models.CASCADE)
    medico=models.ForeignKey(medico,on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} - {}'.format(self.pacientes, self.medico, self.fecha)


    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'