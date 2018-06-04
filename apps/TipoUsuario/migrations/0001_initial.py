# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-06-04 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(choices=[('Administrador', 'Administrador'), ('Estudiante', 'Estudiante'), ('Profesor', 'Profesor')], default='--------', help_text='Seleccione el tipo usuario', max_length=20)),
            ],
        ),
    ]
