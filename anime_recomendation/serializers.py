from rest_framework import serializers
from .models import ani_model

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ani_model
        fields = ['id', 'name', 'genre', 'rating']