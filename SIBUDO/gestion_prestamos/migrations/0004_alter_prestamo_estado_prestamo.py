# Generated by Django 4.2.1 on 2023-07-16 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_prestamos', '0003_disponible_a_prestamo_delete_disponibile_a_prestamos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='estado_prestamo',
            field=models.IntegerField(),
        ),
    ]
