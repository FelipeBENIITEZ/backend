from django.urls import include, path
from rest_framework import routers
from .views import InscripcionViewSet,ArancelViewSet



router = routers.DefaultRouter()
router.register(r'inscripciones', InscripcionViewSet, basename='inscripcion')
router.register(r'aranceles', ArancelViewSet, basename='aranceles')

urlpatterns = [
    path('', include(router.urls)),
    
]
