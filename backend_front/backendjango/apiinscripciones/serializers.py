from rest_framework import serializers
from .models import Inscripcion, Arancel
from apitutores.serializers import TutorAlumnoSerializer
from rest_framework import serializers
from .models import Inscripcion, Arancel
class ArancelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arancel
        fields = '__all__'

class InscripcionSerializer(serializers.ModelSerializer):
    aranceles = ArancelSerializer(many=True, read_only=True)
    tutor_alumno = TutorAlumnoSerializer()

    class Meta:
        model = Inscripcion
        fields = '__all__'
