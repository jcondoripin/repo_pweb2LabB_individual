# Generated by Django 4.2.2 on 2023-07-03 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinos', '0005_destino_tipodescuento_alter_destino_descuento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destino',
            name='tipoDescuento',
        ),
        migrations.AlterField(
            model_name='destino',
            name='descuento',
            field=models.IntegerField(blank=True, default=0, help_text='Descuento establecido por oferta (porcentaje 0 - 100)'),
        ),
    ]
