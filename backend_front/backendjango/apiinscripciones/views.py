from rest_framework import viewsets
from .models import Inscripcion
from .models import Arancel
from .serializers import InscripcionSerializer,ArancelSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
class ArancelViewSet(viewsets.ModelViewSet):
    queryset = Arancel.objects.all()
    serializer_class = ArancelSerializer

