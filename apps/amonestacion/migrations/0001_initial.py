# Generated by Django 2.2.7 on 2019-11-14 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('horaClase', '0001_initial'),
        ('personal', '0001_initial'),
        ('falta', '0001_initial'),
        ('sancion', '0001_initial'),
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amonestacion',
            fields=[
                ('idAmonestacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiante.Estudiante')),
                ('falta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='falta.Falta')),
                ('horario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='horaClase.HoraClase')),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Personal')),
                ('sancion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sancion.Sancion')),
            ],
        ),
    ]
