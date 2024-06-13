from rest_framework import serializers
from .models import Tutor,TutorAlumno
from apialumnos.serializers import AlumnoSerializer
class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'
class TutorAlumnoSerializer(serializers.ModelSerializer):
    alumno = AlumnoSerializer()
    tutor = TutorSerializer()
    class Meta:
        model = TutorAlumno
        fields = '__all__'