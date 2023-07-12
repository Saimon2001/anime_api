from rest_framework import viewsets
from anime_info.models import info
from .serializers import AnimeSerializer
from rest_framework import generics

# Create your views here.

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = info.objects.all()
    serializer_class = AnimeSerializer

class AnimeGeneric(generics.ListCreateAPIView):
    queryset = info.objects.all()
    serializer_class = AnimeSerializer

    def get_queryset(self):
        queryset = super(AnimeGeneric, self).get_queryset()
        user = self.request.user
        if not self.request.user.is_superuser:
            queryset.objects.filter(estado=True)
        return queryset


    def get(self, request, *args, **kwargs):
        """Prueba de documentación

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        print("Hola entre al get")
        return super(AnimeGeneric, self).get(request, *args, **kwargs)



class AnimeGenericDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = info.objects.all()
    serializer_class = AnimeSerializer

    def retrieve(self, request, *args, **kwargs):
        print("Soy retrieve")
        return super(AnimeGenericDetail, self).retrieve(request, *args, **kwargs)