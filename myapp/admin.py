from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
#from .models import Estudiantes_septimo
#from .models import Estudiantes_octavo

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from django.contrib import admin
import datetime
import calendar
from django.urls import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
from myapp import models

# Register your models here.


admin.site.register(models.Subir_Diurno)
admin.site.register(models.Subir_Nocturno)


#admin.site.register(Estudiantes_septimo)
#admin.site.register(Estudiantes_octavo)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('usuario')
    #pass

"""
class Estudiantes_septimoInLine(admin.TabularInline):
    model = Estudiantes_septimo

@admin.register(Estudiantes_septimo)
class Estudiantes_septimoAdmin(admin.ModelAdmin):
    list_filter = ('asistencia', 'Fecha')
    fieldsets = (
        ('Estudiante', {
            'fields': ('usuario','nombre', 'primer_apellido', 'segundo_apellido')
        }),
        ('Asistencia', {
            'fields': ('asistencia', 'Fecha')
        }),
    )
    #inlines=['asistencia', 'Fecha']


@admin.register(Estudiantes_octavo)
class Estudiantes_octavoAdmin(admin.ModelAdmin):
    list_filter = ('asistencia', 'Fecha')
    fieldsets = (
        ('Estudiante', {
            'fields': ('usuario','nombre', 'primer_apellido', 'segundo_apellido')
        }),
        ('Asistencia', {
            'fields': ('asistencia', 'Fecha')
        }),
    )
"""
