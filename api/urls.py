from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import AnimeViewSet, AnimeGenericDetail, AnimeGeneric
from rest_framework.documentation import include_docs_urls

router = SimpleRouter()

router.register(r'info', AnimeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('anime/generics/', AnimeGeneric.as_view()),
    path('anime/generics/<int:pk>/', AnimeGenericDetail.as_view()),
    path('docs/', include_docs_urls(title='My Anime documentation'))
]