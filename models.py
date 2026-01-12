from django.db import models

class PlatoTipico(models.Model):
    REGIONES = [
        ('Costa', 'Costa'),
        ('Sierra', 'Sierra'),
        ('Oriente', 'Amazonía'),
        ('Insular', 'Galápagos'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name="Descripción")
    region = models.CharField(max_length=20, choices=REGIONES)
    precio_sugerido = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre
