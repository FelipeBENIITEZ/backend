from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from .models import Inscripcion, Arancel
from apitutores.models import *
def generar_pagare_pdf(request, id):
    inscripcion = get_object_or_404(Inscripcion, id=id)
    tutor_alumno = inscripcion.tutor_alumno
    arancel = inscripcion.aranceles.first()

    tutor_nombre = tutor.tut_nom
    tutor_apellido = tutor.tut_ape
    tutor_direccion = tutor.tut_direc
    tutor_ci = tutor.tut_ci
    alumno_nombre = alumno.alum_nom
    alumno_apellido = alumno.alum_ape
    arancel_matricula = arancel.arancel_matricula
    arancel_cuota = arancel.arancel_cuota
    arancel_nivel = arancel.arancel_nivel
    arancel_grado = arancel.arancel_grado

    pagare_content = [
        ("PAGARÉ", "CENTER", True),
        (f"Yo, {tutor_nombre} {tutor_apellido}, con C.I. {tutor_ci} y domiciliado en {tutor_direccion}, me obligo a pagar a la orden del CENTRO EDUCATIVO PARAGUAY - BRASIL (CEPB) la suma de {arancel_matricula + arancel_cuota} guaraníes.", "JUSTIFY", False),
        (f"Este pagaré corresponde al pago de la matrícula y la cuota del estudiante {alumno_nombre} {alumno_apellido}.", "JUSTIFY", False),
        (f"La suma mencionada será pagada en cuotas mensuales de {arancel_cuota} guaraníes cada una, con vencimiento el primer día de cada mes.", "JUSTIFY", False),
        ("En caso de mora en el pago de cualquier cuota, se aplicará un recargo del 15% mensual sobre el monto adeudado.", "JUSTIFY", False),
        ("Lugar y Fecha", "LEFT", True),
        ("____________________________", "LEFT", True),
        ("Firma del Deudor", "LEFT", True),
    ]

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="pagare_{inscripcion.id}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    style_center = ParagraphStyle(name="Center", alignment=TA_CENTER)
    style_left = ParagraphStyle(name="Left", alignment=TA_LEFT)
    style_justify = ParagraphStyle(name="Justify", alignment=TA_JUSTIFY)

    for text, alignment, is_bold in pagare_content:
        style = style_center if alignment == "CENTER" else (style_left if alignment == "LEFT" else style_justify)
        if is_bold:
            style.fontName = "Helvetica-Bold"
        elements.append(Paragraph(text, style))

    doc.build(elements)

    return response
