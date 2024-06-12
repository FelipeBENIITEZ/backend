from django.urls import path, include
from rest_framework import routers
from .views import TutorViewSet, TutorAlumnoViewSet
 
router = routers.DefaultRouter()
router.register(r'tutores', TutorViewSet)
router.register(r'tutor_alumnos', TutorAlumnoViewSet)
 
urlpatterns = [
    path('api/v1/', include(router.urls)),
]