# Generated by Django 3.1.2 on 2020-10-15 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appconsultaeps', '0003_citas_especialista_grupo_familiar_historia_clinica_medico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 15, 11, 32, 11, 577246)),
        ),
    ]
