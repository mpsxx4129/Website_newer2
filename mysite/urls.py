"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from myapp import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django_downloadview import ObjectDownloadView

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', v.diurno, name='diurno'),
    path('diurno/', v.diurno, name='diurno'),
    path('index/', v.index, name='index'),
    path('nocturno/', v.nocturno, name='nocturno'),
    path('anuNoct/', v.anuNoct, name='anuNoct'),
    path('anuDi/', v.anuDi, name='anuDi'),
    path('contact/', v.contact, name='contact'),
    path('acerca/', v.acerca, name='acerca'),
    path('calendario/', v.calendario, name='calendario'),
    path('matricula/', v.matricula, name='matricula'),
    path('objetivos/', v.objetivos, name='objetivos'),
    path('admision/', v.admision, name='admision'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('download/', v.download, name='download'),
    path('downloaddos/', v.downloaddos, name='downloaddos'),
    path('valores/',v.valores,  name='valores'),
    path('TCU/',v.TCU,  name='TCU'),
    path('hist/',v.hist,  name='hist'),

]

urlpatterns += staticfiles_urlpatterns()
