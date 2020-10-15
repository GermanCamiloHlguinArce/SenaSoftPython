from django.db import models
from django.contrib.auth.models import AbstractUser, User


class tipo_doc (models.Model):
    doc=models.CharField(max_length=20, null=False,blank=False)

    def __str__(self):
        return self.doc


class pacientes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    edad=models.PositiveIntegerField()
    peso=models.PositiveIntegerField()
    estatura=models.PositiveIntegerField()
    estado_civil=models.CharField(max_length=45, null=False,blank=False)
    tipo_doc=models.ForeignKey(tipo_doc, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.user.first_name)


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



class especialista(models.Model):
    especialidad=models.CharField(max_length=50,null=False,blank=False)


class medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='medico')
    numero_doc = models.PositiveIntegerField()
    telefono = models.PositiveIntegerField()
    tipo_doc = models.ForeignKey(tipo_doc, on_delete=models.CASCADE)
    especialista = models.ForeignKey(especialista, on_delete=models.CASCADE)



class citas(models.Model):
    fecha=models.DateTimeField()
    pacientes=models.ForeignKey(pacientes,on_delete=models.CASCADE)
    medico=models.ForeignKey(medico,on_delete=models.CASCADE)



class grupo_familiar(models.Model):
    parentesco=models.CharField(max_length=50,null=False,blank=False)
    pacientes=models.ForeignKey(pacientes,on_delete=models.CASCADE)
    medico=models.ForeignKey(medico,on_delete=models.CASCADE)

