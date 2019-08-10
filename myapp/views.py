from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views import generic
#from .models import Estudiantes_septimo
#from .models import Estudiantes_octavo
#from .models import Datos
#from .forms import dataForm
from django.db import models
import datetime
from django.http import HttpResponse
import glob
import os
import re
import os.path

# Create your views here.


#@login_required
def index(request):
	return render_to_response('index.html')

def contact(request):
    return render_to_response('contact.html')

def acerca(request):
    return render_to_response('acerca.html')

def calendario(request):
    return render_to_response('calendario.html')

def matricula(request):
    return render_to_response('matricula.html')

def objetivos(request):
    return render_to_response('objetivos.html')

def diurno(request):
    return render_to_response('diurno.html')

def nocturno(request):
    return render_to_response('nocturno.html')

def admision(request):
    return render_to_response('admision.html')

def valores(request):
    return render_to_response('valores.html')

def TCU(request):
    return render_to_response('TCU.html')

def hist(request):
    return render_to_response('hist.html')

def anuDi(request):
    return render_to_response('anuDi.html')

def anuNoct(request):
    return render_to_response('anuNoct.html')

def download(request):
    path = "download/*.pdf"
    for filename in glob.glob(path):
        if os.path.isfile(filename):
            with open(filename, 'rb') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename=some_file.pdf'
                return response
                pdf.closed
        else:
            break
    return render_to_response('anuDi.html')

def downloaddos(request):
    path = "downloaddos/*.pdf"
    for filename in glob.glob(path):
        if os.path.isfile(filename):
            with open(filename, 'rb') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename=some_file.pdf'
                return response
                pdf.closed
        else:
            break
    return render_to_response('anuNoct.html')


"""
class AnuncioList(LoginRequiredMixin, generic.ListView):
    model = Anuncio
    queryset = Anuncio.objects.all()
    def get_queryset(self):
        return Anuncio.objects.all()





class AsistenciaList(LoginRequiredMixin, generic.ListView):



    model = Estudiantes_septimo

    template_name ='asistencia.html'

    queryset = Estudiantes_septimo.objects.all()

    def get_queryset(self):
        if hasattr(Estudiantes_septimo,'usuario'):
            return Estudiantes_septimo.objects.all()
        else:
            return Estudiantes_octavo.objects.filter(asistencia='Asistio')



def get_data(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = dataForm(request.POST)
        print(request.POST)


        dataForm.ausentismo = request.POST.get('asusentismo')
        dataForm.bajas_calificaciones = request.POST.get('calificaciones','')
        dataForm.falta_recursos = request.POST.get('reursos','')
        dataForm.problemas = request.POST.get('familiares','')
        dataForm.violencia = request.POST.get('Violencia','')
        dataForm.adicciones = request.POST.get('Adicciones','')
        dataForm.interes = request.POST.get('interes','')
        dataForm.tardias = request.POST.get('tardias','')
        dataForm.comportamiento = request.POST.get('comportamiento','')
        dataForm.trabajos = request.POST.get('trabajos','')
        dataForm.otros = request.POST.get('otros','')

        toSave = Datos(otros=dataForm.ausentismo, trabajos=dataForm.trabajos,
        comportamiento=dataForm.comportamiento, tardias=dataForm.tardias,
        interes=dataForm.interes,adicciones=dataForm.adicciones,
        violencia=dataForm.violencia, problemas=dataForm.problemas,
        falta_recursos=dataForm.falta_recursos, bajas_calificaciones=dataForm.bajas_calificaciones,
        ausentismo=dataForm.ausentismo)
        toSave.save()
        return HttpResponseRedirect('/asistencia')

        # check whether it's valid:


        return render_to_response('asistencia.html', {'form':dataForm()}, RequestContext(request))

        if form.is_valid():
            print("hola")
            form.save()

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('asistencia.html')
        else:
            print("hdola")
            form = dataForm()


    return render(request, 'asistencia.html')


def subir(request):

     if request.method == "POST":
         nombre_id = request.POST.get('nombre-id', None)

         # TODO toggle the order here
"""
