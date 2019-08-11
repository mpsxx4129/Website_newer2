# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Subir_Diurno(models.Model):
    pdf = models.FileField(upload_to='download/')


class Subir_Nocturno(models.Model):
    pdf = models.FileField(upload_to='downloaddos/')

@receiver(post_delete, sender=Subir_Diurno)
@receiver(post_delete, sender=Subir_Nocturno)
def submission_delete(sender, instance, **kwargs):
    instance.pdf.delete(False)



"""
class Estudiantes_septimo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, )
    nombre = models.CharField(max_length=30, default="Ingrese primer nombre")
    primer_apellido = models.CharField(max_length=30, default="Ingrese Primer apellido")
    segundo_apellido = models.CharField(max_length=30, default="Ingrese Segundo Apellido")
    Fecha = models.DateField(null=True, blank=True)


    asistio='A'
    no_asistio='N/A'

    asistencia_choices=(
    (asistio, 'Asistio'),
    (no_asistio, 'No asistio')
    )

    asistencia = models.CharField(max_length=2,default=asistio,choices=asistencia_choices)

    def __str__(self):
	    return (self.nombre+ " " + self.primer_apellido +" "+ self.segundo_apellido)

	# Metadata
    class Meta:
        ordering = ["-usuario"]


class Estudiantes_octavo(models.Model):

    nombre = models.CharField(max_length=30, default="Ingrese primer nombre")
    primer_apellido = models.CharField(max_length=30, default="Ingrese Primer apellido")
    segundo_apellido = models.CharField(max_length=30, default="Ingrese Segundo Apellido")
    Fecha = models.DateField(null=True, blank=True)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    asistio='A'
    no_asistio='N/A'

    asistencia_choices=(
    (asistio, 'Asistio'),
    (no_asistio, 'No asistio')
    )

    asistencia = models.CharField(max_length=2,default=asistio,choices=asistencia_choices)

    def __str__(self):
	    return (self.nombre+ " " + self.primer_apellido +" "+ self.segundo_apellido)

	# Metadata
    class Meta:
        ordering = ["-usuario"]

class Datos(models.Model):
    bajas_calificaciones = models.CharField(max_length=30, default=' STRING')
    ausentismo = models.CharField(max_length=30, default=' STRING')
    falta_recursos = models.CharField(max_length=30, default=' STRING')
    problemas = models.CharField(max_length=30, default=' STRING')
    violencia = models.CharField(max_length=30, default=' STRING')
    adicciones = models.CharField(max_length=30, default=' STRING')
    interes= models.CharField(max_length=30, default=' STRING')
    tardias= models.CharField(max_length=30, default=' STRING')
    comportamiento= models.CharField(max_length=30, default=' STRING')
    trabajos= models.CharField(max_length=30, default=' STRING')
    otros= models.CharField(max_length=30, default=' STRING')
"""
"""
a_record = Estudiante(assis = "Instancia #1")
a_record.save()

a_record.my_field_name="Nuevo Nombre de Instancia"
a_record.save()

all_students = Estudiante.objects.all()
students_assistance = Estudiante.objects.filter(title__contains='wild')
"""
