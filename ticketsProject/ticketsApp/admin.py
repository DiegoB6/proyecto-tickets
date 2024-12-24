from django.contrib import admin

from ticketsApp.models import *

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    list_display = ['id', 'servicio']
admin.site.register(Servicio,ServicioAdmin)


class TipoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo']
admin.site.register(Tipo,TipoAdmin)


class CriticidadAdmin(admin.ModelAdmin):
    list_display = ['id', 'criticidad']
admin.site.register(Criticidad,CriticidadAdmin)


class EstadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'estado']
admin.site.register(Estado,EstadoAdmin)


class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'area']
admin.site.register(Area,AreaAdmin)



class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'telefono', 'correo', 'nombre', 'rut']
admin.site.register(Usuario,UsuarioAdmin)


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'detalle', 'observacion', 'servicio', 'tipo', 'criticidad', 'estado', 'area']
admin.site.register(Ticket,TicketAdmin)