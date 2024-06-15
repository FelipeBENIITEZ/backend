from django.db import models
from apitutores.models import *
from apialumnos.models import *
from django.dispatch import receiver
from django.db.models.signals import pre_save
class Inscripcion(models.Model):
    tutor_alumno = models.ForeignKey('apitutores.TutorAlumno', on_delete=models.CASCADE)
    ins_fecha = models.DateField(auto_now_add=True)
    ins_descuento = models.PositiveIntegerField(default=0, editable=False)
    ins_contrato_fecha = models.DateField()
    ins_cuota = models.PositiveIntegerField(editable=False)
    ESTADO_CHOICES = (
        ('Pagado', 'Pagado'),
        ('Pendiente', 'Pendiente'),
        ('Inscripto', 'Inscripto'),
    )
    ins_estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    ins_hab = models.BooleanField(default=True)
    ins_periodo = models.CharField(max_length=4)

    def save(self, *args, **kwargs):
        # Obtener el tutor y contar las inscripciones existentes para este tutor
        tutor = self.tutor_alumno.tutor
        inscripciones_existentes = Inscripcion.objects.filter(tutor_alumno__tutor=tutor).count()

        # Calcular el descuento basado en el número de hijos ya inscritos
        if tutor.tut_tipo in ['Padre', 'Madre', 'Tutor legal']:
            self.ins_descuento = max(0, inscripciones_existentes * 50000)
        else:
            self.ins_descuento = 0
        
        # Calcular la cuota después de aplicar el descuento
        self.ins_cuota = 500000 - self.ins_descuento

        super().save(*args, **kwargs)

    def __str__(self):
     return f"Inscripción de {self.tutor_alumno.alumno} con {self.tutor_alumno.tutor} - {self.ins_fecha}"

class Arancel(models.Model):
    inscripcion = models.ForeignKey('apiinscripciones.Inscripcion', related_name='aranceles', on_delete=models.CASCADE)
    arancel_nivel = models.CharField(max_length=20, choices=[('Escolar Básica', 'Escolar Básica'), ('Nivel Inicial', 'Nivel Inicial'), ('Educación Media', 'Educación Media')])
    arancel_ciclo = models.CharField(max_length=20, choices=[('Preescolar', 'Preescolar'), ('1º', '1º'), ('2º', '2º'), ('3º', '3º'), ('Bachillerato', 'Bachillerato')], null=True, blank=True)
    arancel_especializacion = models.CharField(max_length=20, choices=[('BTI', 'BTI'), ('BTA', 'BTA'), ('Ciencias Sociales', 'Ciencias Sociales'), ('Ciencias Básicas', 'Ciencias Básicas')], null=True, blank=True)
    arancel_grado = models.CharField(max_length=20, choices=[('Pre Jardín', 'Pre Jardín'), ('Jardín', 'Jardín'), ('Preescolar', 'Preescolar'), ('1º', '1º'), ('2º', '2º'), ('3º', '3º'), ('4º', '4º'), ('5º', '5º'), ('6º', '6º'), ('7º', '7º'), ('8º', '8º'), ('9º', '9º'), ('1º Bachillerato', '1º Bachillerato'), ('2º Bachillerato', '2º Bachillerato'), ('3º Bachillerato', '3º Bachillerato')], null=True, blank=True)
    arancel_turno = models.CharField(max_length=20, choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde')], null=True, blank=True)
    arancel_matricula = models.PositiveIntegerField(editable=False)
    arancel_cuota = models.PositiveIntegerField(editable=False)
      
    def save(self, *args, **kwargs):
        # Obtener la inscripción relacionada
        inscripcion = self.inscripcion

        # Establecer el valor de arancel_matricula igual a ins_cuota de la inscripción
        self.arancel_matricula = inscripcion.ins_cuota
        super().save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.arancel_nivel == 'Nivel Inicial':
            self.arancel_cuota = 500000
        elif self.arancel_nivel == 'Escolar Básica':
            if self.arancel_turno == 'Mañana':
                self.arancel_cuota = 500000
            elif self.arancel_turno == 'Tarde':
                self.arancel_cuota = 400000
        elif self.arancel_nivel == 'Educación Media':
            if self.arancel_especializacion in ['Ciencias Sociales', 'Ciencias Básicas']:
                self.arancel_cuota = 600000
            elif self.arancel_especializacion in ['BTI', 'BTA']:
                self.arancel_cuota = 800000
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.inscripcion} - {self.arancel_nivel} - {self.arancel_cuota}"

@receiver(pre_save, sender=Arancel)
def set_arancel_matricula(sender, instance, **kwargs):
    if instance.inscripcion:
        instance.arancel_matricula = instance.inscripcion.ins_cuota

# Create your models here.
