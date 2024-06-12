from django.contrib import admin
from .models import Inscripcion,Arancel
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'tutor_alumno', 'ins_fecha', 'ins_descuento', 'ins_contrato_fecha')
    search_fields = ('tutor_alumno__tutor__tut_nom', 'tutor_alumno__alumno__alum_nom')
    list_filter = ('ins_fecha', 'ins_descuento')
class ArancelAdmin(admin.ModelAdmin):
    list_display = ['inscripcion', 'arancel_nivel', 'arancel_cuota']
    readonly_fields = ('arancel_cuota', 'arancel_matricula')
admin.site.register(Inscripcion, InscripcionAdmin)
admin.site.register(Arancel, ArancelAdmin)
# Register your models here.
