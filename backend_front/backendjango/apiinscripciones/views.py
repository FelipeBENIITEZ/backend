from rest_framework import viewsets
from .models import Inscripcion, Arancel
from .serializers import InscripcionSerializer, ArancelSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.filter(aranceles__isnull=False).distinct()  # Filtrar inscripciones con aranceles
    serializer_class = InscripcionSerializer

class ArancelViewSet(viewsets.ModelViewSet):
    queryset = Arancel.objects.all()
    serializer_class = ArancelSerializer
