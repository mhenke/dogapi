from django.urls import include, path
from rest_framework import routers
from .views import BreedViewSet, DogViewSet

router = routers.DefaultRouter()
router.register(r'breeds', BreedViewSet)
router.register(r'dogs', DogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]