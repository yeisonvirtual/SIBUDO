# Generated by Django 4.2.1 on 2023-07-27 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_recursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='isbn',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
