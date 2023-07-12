from anime_info.views import tarea_celery
from django.urls import path

urlpatterns = [
    path("tarea_celery", tarea_celery),
]