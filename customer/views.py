from django.shortcuts import render
# from django.http import HttpResponse
# from anime_recomendation.models import ani_model
# # Create your views here.

# def crear_objeto(request):
#     category = ani_model(name="Prueba 3")
#     category.save()
#     category = ani_model.objects.create(name="Prueba 4")
#     return HttpResponse(category.name)

from django.core.cache import cache

# Create your views here.
def prueba_cache(request):

    cache.set("my_key", "Token Anime", 600)

    value = cache.get("my_key")

    return HttpResponse("La cache fue creada y consultada")
