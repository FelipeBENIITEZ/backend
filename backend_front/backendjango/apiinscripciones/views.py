from rest_framework import viewsets
from .models import Inscripcion
from .serializers import InscripcionSerializer
 
class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer