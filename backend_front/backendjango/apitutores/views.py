from rest_framework import viewsets
from .models import Tutor, TutorAlumno
from .serializers import TutorSerializer, TutorAlumnoSerializer
 
class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
 
class TutorAlumnoViewSet(viewsets.ModelViewSet):
    queryset = TutorAlumno.objects.all()
    serializer_class = TutorAlumnoSerializer