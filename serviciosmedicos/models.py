from django.db import models

# Create your models here.
class Profesionales(models.Model):
    profesional=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(blank=True,null=True)
    telefono=models.CharField(blank=True,null=True,max_length=20)
    password=models.CharField(max_length=10)
    class Meta:
        verbose_name='profesional'
        verbose_name_plural='profesionales'
    def __str__(self):
        return self.profesional

class Servicios(models.Model):
    servicio=models.CharField(max_length=20)
    consultorio=models.BooleanField()
    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    def __str__(self):
        return self.servicio

class Atencion(models.Model):
    servicio=models.ForeignKey(Servicios, on_delete=models.CASCADE)
    profesional=models.ForeignKey(Profesionales, on_delete=models.CASCADE)
    lunes=models.BooleanField()
    martes=models.BooleanField()
    miercoles=models.BooleanField()
    jueves=models.BooleanField()
    viernes=models.BooleanField()
    class Meta:
        verbose_name='atencion'
        verbose_name_plural='atenciones'