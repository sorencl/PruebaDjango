# Generated by Django 3.2.4 on 2021-07-08 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('rutPersona', models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut persona')),
                ('nombrePersona', models.CharField(max_length=50, verbose_name='Nombre de la Persona')),
                ('numTelefono', models.CharField(max_length=12, verbose_name='Numero de telefono')),
            ],
        ),
        migrations.CreateModel(
            name='Vehichulo',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Patente')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('modelo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo')),
                ('color', models.CharField(max_length=15, verbose_name='Color')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.persona')),
            ],
        ),
    ]
