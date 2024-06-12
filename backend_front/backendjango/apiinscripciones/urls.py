from django.urls import include, path
from rest_framework import routers
from .views import InscripcionViewSet
 
router = routers.DefaultRouter()
router.register(r'inscripciones', InscripcionViewSet, basename='inscripcion')
 
urlpatterns = [
    path('api/v1/', include(router.urls)),
]