from django.db import models

class Perfiles(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    mail = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    contraseña = models.CharField(max_length=128, verbose_name="Contraseña")

    def __str__(self):
        return self.nombre

class Presupuesto(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto del Presupuesto")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    def __str__(self):
        return f"Presupuesto: ${self.monto}"

class Cotizacion(models.Model):
    descripcion = models.CharField(max_length=255, verbose_name="Descripción")
    unidades = models.PositiveIntegerField(verbose_name="Unidades")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio por Unidad")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total", editable=False)

    def save(self, *args, **kwargs):
        self.total = self.unidades * self.precio
        super().save(*args, **kwargs)

    def __str__(self):
        return self.descripcion
