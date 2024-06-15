from django.urls import path
from .views import generar_contrato, generar_pagare, generar_ficha

urlpatterns = [
    path('generar_contrato/<int:tutor_alumno_id>/', generar_contrato, name='generar_contrato'),
    path('generar_pagare/<int:tutor_alumno_id>/', generar_pagare, name='generar_pagare'),
    path('generar_ficha/<int:tutor_alumno_id>/', generar_ficha, name='generar_ficha'),
]
