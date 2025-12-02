
from django.contrib import admin
from .models import Destino, Vuelo, Alojamiento, Paquete_Turistico, Cliente_Viajes, Reserva_Viaje, Agente_Viajes

admin.site.register(Destino)
admin.site.register(Vuelo)
admin.site.register(Alojamiento)
admin.site.register(Paquete_Turistico)
admin.site.register(Cliente_Viajes)
admin.site.register(Reserva_Viaje)
admin.site.register(Agente_Viajes)
