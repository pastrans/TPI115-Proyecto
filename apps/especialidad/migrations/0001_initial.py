# Generated by Django 2.2.7 on 2019-11-14 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('idEspecialidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('A', 'ACTIVO'), ('B', 'INACTIVO')], default='A', max_length=1)),
            ],
        ),
    ]
