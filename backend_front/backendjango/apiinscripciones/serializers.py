from rest_framework import serializers
from .models import Inscripcion, Arancel
from apitutores.serializers import TutorSerializer, AlumnoSerializer
from rest_framework import serializers


class ArancelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arancel
        fields = '__all__'

class InscripcionSerializer(serializers.ModelSerializer):
    alumno = AlumnoSerializer(read_only=True)
    tutor = TutorSerializer(read_only=True)

    class Meta:
        model = Inscripcion
        fields = '__all__'