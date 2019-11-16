# Generated by Django 2.2.7 on 2019-11-14 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tiempo',
            fields=[
                ('idTiempo', models.AutoField(primary_key=True, serialize=False)),
                ('horaInicial', models.TimeField()),
                ('horaFinal', models.TimeField()),
                ('estado', models.CharField(choices=[('A', 'ACTIVA'), ('I', 'INACTIVA')], default='A', max_length=1)),
            ],
        ),
    ]