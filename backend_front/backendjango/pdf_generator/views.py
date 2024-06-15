from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from io import BytesIO
from apitutores.models import TutorAlumno
from apiinscripciones.models import Inscripcion, Arancel

def generar_pagare(request, tutor_alumno_id):
    try:
        tutor_alumno = TutorAlumno.objects.get(id=tutor_alumno_id)
    except TutorAlumno.DoesNotExist:
        return HttpResponse("Tutor-Alumno no encontrado", status=404)

    inscripcion = Inscripcion.objects.filter(tutor_alumno=tutor_alumno).order_by('-ins_fecha').first()
    if not inscripcion:
        return HttpResponse("No se encontró inscripción para este tutor-alumno", status=404)

    aranceles = Arancel.objects.filter(inscripcion=inscripcion)

    arancel_matricula = 0
    arancel_cuota = 0
    for arancel in aranceles:
        arancel_matricula += arancel.arancel_matricula
        arancel_cuota += arancel.arancel_cuota

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="pagare.pdf"'

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    content = []

    tutor_nombre = tutor_alumno.tutor.tut_nom
    tutor_apellido = tutor_alumno.tutor.tut_ape
    tutor_ci = tutor_alumno.tutor.tut_ci
    tutor_direccion = tutor_alumno.tutor.tut_direc
    alumno_nombre = tutor_alumno.alumno.alum_nom
    alumno_apellido = tutor_alumno.alumno.alum_ape

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

    for text, align, space in pagare_content:
        style = ParagraphStyle(name=f'{align}', alignment=eval(f'TA_{align.upper()}'))
        content.append(Paragraph(text, style))

    doc.build(content)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def generar_contrato(request, tutor_alumno_id):
    try:
        tutor_alumno = TutorAlumno.objects.get(id=tutor_alumno_id)
    except TutorAlumno.DoesNotExist:
        return HttpResponse("Tutor-Alumno no encontrado", status=404)

    inscripcion = Inscripcion.objects.filter(tutor_alumno=tutor_alumno).order_by('-ins_fecha').first()
    if not inscripcion:
        return HttpResponse("No se encontró inscripción para este tutor-alumno", status=404)

    aranceles = Arancel.objects.filter(inscripcion=inscripcion)

    arancel_matricula = 0
    arancel_cuota = 0
    for arancel in aranceles:
        arancel_matricula += arancel.arancel_matricula
        arancel_cuota += arancel.arancel_cuota

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contrato.pdf"'

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    content = []

    tutor_nombre = tutor_alumno.tutor.tut_nom
    tutor_apellido = tutor_alumno.tutor.tut_ape
    tutor_ci = tutor_alumno.tutor.tut_ci
    tutor_direccion = tutor_alumno.tutor.tut_direc
    alumno_nombre = tutor_alumno.alumno.alum_nom
    alumno_apellido = tutor_alumno.alumno.alum_ape

    contrato_content = [
        ("CONTRATO DE SERVICIO EDUCATIVO", "CENTER", True),
        (f"Entre {tutor_nombre} {tutor_apellido}, con C.I. {tutor_ci} y domiciliado en {tutor_direccion}, en calidad de tutor del estudiante {alumno_nombre} {alumno_apellido}, por una parte,", "JUSTIFY", False),
        ("Y", "CENTER", True),
        ("CENTRO EDUCATIVO PARAGUAY - BRASIL (CEPB), por otra parte,", "JUSTIFY", False),
        ("Se acuerda el siguiente contrato de servicio educativo:", "JUSTIFY", False),
        ("...", "JUSTIFY", False),  # Detalles adicionales del contrato
        ("Firmado digitalmente,", "RIGHT", True),
    ]

    for text, align, space in contrato_content:
        style = ParagraphStyle(name=f'{align}', alignment=eval(f'TA_{align.upper()}'))
        content.append(Paragraph(text, style))

    doc.build(content)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def generar_ficha(request, tutor_alumno_id):
    try:
        tutor_alumno = TutorAlumno.objects.get(id=tutor_alumno_id)
    except TutorAlumno.DoesNotExist:
        return HttpResponse("Tutor-Alumno no encontrado", status=404)

    inscripcion = Inscripcion.objects.filter(tutor_alumno=tutor_alumno).order_by('-ins_fecha').first()
    if not inscripcion:
        return HttpResponse("No se encontró inscripción para este tutor-alumno", status=404)

    aranceles = Arancel.objects.filter(inscripcion=inscripcion)

    arancel_matricula = 0
    arancel_cuota = 0
    for arancel in aranceles:
        arancel_matricula += arancel.arancel_matricula
        arancel_cuota += arancel.arancel_cuota

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ficha.pdf"'

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    content = []

    tutor_nombre = tutor_alumno.tutor.tut_nom
    tutor_apellido = tutor_alumno.tutor.tut_ape
    tutor_ci = tutor_alumno.tutor.tut_ci
    tutor_direccion = tutor_alumno.tutor.tut_direc
    alumno_nombre = tutor_alumno.alumno.alum_nom
    alumno_apellido = tutor_alumno.alumno.alum_ape

    ficha_content = [
        ("FICHA DE INSCRIPCIÓN", "CENTER", True),
        (f"Nombre del estudiante: {alumno_nombre} {alumno_apellido}", "JUSTIFY", False),
        (f"Tutor: {tutor_nombre} {tutor_apellido}", "JUSTIFY", False),
        ("...", "JUSTIFY", False),  # Detalles adicionales de la ficha
        ("Firmado digitalmente,", "RIGHT", True),
    ]

    for text, align, space in ficha_content:
        style = ParagraphStyle(name=f'{align}', alignment=eval(f'TA_{align.upper()}'))
        content.append(Paragraph(text, style))

    doc.build(content)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

