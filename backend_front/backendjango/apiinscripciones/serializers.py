from rest_framework import serializers
from .models import Inscripcion, Arancel
from apitutores.serializers import TutorAlumnoSerializer

class InscripcionSerializer(serializers.ModelSerializer):
    tutor_alumno = TutorAlumnoSerializer()

    class Meta:
        model = Inscripcion
        fields = '__all__'

class ArancelSerializer(serializers.ModelSerializer):
    # Se define InscripcionSerializer como un campo base para evitar recursión infinita
    inscripcion = serializers.PrimaryKeyRelatedField(queryset=Inscripcion.objects.all())

    class Meta:
        model = Arancel
        fields = '__all__'
