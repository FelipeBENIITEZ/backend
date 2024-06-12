from rest_framework import viewsets
from .models import Alumno
from .serializers import AlumnoSerializer
 
class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
