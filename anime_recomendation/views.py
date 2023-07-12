from django.http import JsonResponse
from .models import ani_model
from .serializers import AnimeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

#CRUD
@api_view(['GET', 'POST'])
def anime_list(request, format=None):
    
    if request.method == 'GET':
        anime = ani_model.objects.all()
        serializer = AnimeSerializer(anime, many=True)
        return Response(serializer.data)

    if request.method == 'POST': #update
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def anime_detail(request, id, format=None):

    try:
        anime = ani_model.objects.get(pk=id)
    except ani_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)
    elif request.method == 'PUT': #update
        serializer = AnimeSerializer(anime, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        anime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

