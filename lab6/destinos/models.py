from django.db import models

# Create your models here.
class Destino(models.Model):

    nombre = models.TextField(blank=False, unique=True, null=False, help_text="Nombre de esta ciudad de destino turístico", max_length=50)

    descripcion = models.TextField(blank=False, null=False, help_text="Descripción de esta ciudad de destino turístico")

    imagen = models.ImageField(upload_to="destinos", help_text="Imagen de esta ciudad de destino turístico")

    precioTour = models.FloatField(blank=False, null=False, help_text="Precio del tour a esta ciudad de destino turístico")

    oferta = models.BooleanField(default=False, help_text="Decide si el viaje a este destino turístico está de oferta")

    descuento = models.FloatField(default=0, blank=True, help_text="Descuento establecido por oferta (number | percentage)")

    tipoDescuento = models.CharField(null=True, blank=True, choices=[('#', 'number'), ('%', 'percentage')], max_length=1)