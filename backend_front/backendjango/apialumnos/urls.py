from django.urls import include, path
from rest_framework import routers
from .views import AlumnoViewSet
 
router = routers.DefaultRouter()
router.register(r'alumnos', AlumnoViewSet, basename='alumno')
 
urlpatterns = [
    path('api/v1/', include(router.urls)),
]