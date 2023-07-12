from django.shortcuts import render
from django.http import HttpResponse
from .task import tarea_larga

def tarea_celery(request):
    tarea_larga.delay()
    return HttpResponse('Tarea se ejecuto con celery')
