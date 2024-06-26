# Generated by Django 5.0.6 on 2024-06-02 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alum_nom', models.CharField(max_length=100)),
                ('alum_ape', models.CharField(max_length=100)),
                ('alum_fecha_nac', models.DateField()),
                ('alum_edad', models.PositiveIntegerField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tut_tipo', models.CharField(choices=[('Padre', 'Padre'), ('Madre', 'Madre'), ('Tutor legal', 'Tutor legal'), ('Otro', 'Otro')], max_length=20)),
                ('tut_nom', models.CharField(max_length=100)),
                ('tut_ape', models.CharField(max_length=100)),
                ('tut_ci', models.CharField(max_length=20)),
                ('tut_tel', models.CharField(max_length=20)),
                ('tut_direc', models.CharField(max_length=200)),
                ('tut_mail', models.EmailField(max_length=254)),
                ('tut_hijos', models.PositiveIntegerField(default=0, editable=False)),
                ('tut_descuento', models.PositiveIntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='TutorAlumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apialumnos.alumno')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apialumnos.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateField(auto_now_add=True)),
                ('contrato_fecha', models.DateField()),
                ('tutor_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apialumnos.tutoralumno')),
            ],
        ),
    ]
