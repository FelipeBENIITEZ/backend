# Generated by Django 5.0.6 on 2024-06-07 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiinscripciones', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arancel',
            name='arancel_cuota',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='arancel',
            name='arancel_matricula',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
