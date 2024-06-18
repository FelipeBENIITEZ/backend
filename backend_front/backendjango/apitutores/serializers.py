from rest_framework import serializers
from .models import Tutor, TutorAlumno
from apialumnos.serializers import AlumnoSerializer

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class TutorAlumnoSerializer(serializers.ModelSerializer):
    alumno = AlumnoSerializer()
    tutor = TutorSerializer()

    # Aquí configuramos el campo tutor_alumno para que sea el id del objeto TutorAlumno
    tutor_alumno = serializers.PrimaryKeyRelatedField(source='id', queryset=TutorAlumno.objects.all())

    class Meta:
        model = TutorAlumno
        fields = '__all__'
