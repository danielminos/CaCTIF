from django.contrib import admin
from serviciosmedicos.models import Profesionales, Servicios, Atencion

# Register your models here.
class ProfesionalesAdmin(admin.ModelAdmin):
    list_display=("profesional","direccion","email","telefono","password")

class ServiciosAdmin(admin.ModelAdmin):
    list_display=("servicio","consultorio")

class AtencionAdmin(admin.ModelAdmin):
    list_display=("servicio","profesional","lunes","martes","miercoles","jueves","viernes")

admin.site.register(Profesionales,ProfesionalesAdmin)
admin.site.register(Servicios,ServiciosAdmin)
admin.site.register(Atencion,AtencionAdmin)