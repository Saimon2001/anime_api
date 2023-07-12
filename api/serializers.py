from rest_framework import serializers
from anime_info.models import info

class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = info
        fields = ('title', 'description', 'language', 'release_year')

class AnimeSerializerNoORM(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()