from rest_framework import serializers
from .models import Inscripcion, Arancel
from apitutores.serializers import TutorAlumnoSerializer
from rest_framework import serializers
from .models import Inscripcion, Arancel
class ArancelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arancel
        fields = ('id', 'arancel_matricula', 'arancel_cuota', 'arancel_nivel', 'arancel_ciclo', 'arancel_grado')

class InscripcionSerializer(serializers.ModelSerializer):
    aranceles = ArancelSerializer(many=True, read_only=True)
    tutor_alumno = TutorAlumnoSerializer()

    class Meta:
        model = Inscripcion
        fields = ('id','tutor_alumno','ins_contrato_fecha', 'ins_estado', 'ins_periodo', 'aranceles')

