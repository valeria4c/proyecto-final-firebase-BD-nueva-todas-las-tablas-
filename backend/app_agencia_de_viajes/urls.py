from django.urls import path
from .views import (
    # Vistas de la página de inicio
    HomeView,

    # Vistas de Destino
    DestinoListView, DestinoCreateView, DestinoUpdateView, DestinoDeleteView,
    
    # Vistas de Vuelo
    VueloListView, VueloCreateView, VueloUpdateView, VueloDeleteView,

    # Vistas de Alojamiento
    AlojamientoListView, AlojamientoCreateView, AlojamientoUpdateView, AlojamientoDeleteView,

    # Vistas de PaqueteTuristico
    PaqueteTuristicoListView, PaqueteTuristicoCreateView, PaqueteTuristicoUpdateView, PaqueteTuristicoDeleteView,
    
    # Vistas de Cliente
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    
    # Vistas de Reserva
    ReservaListView, ReservaCreateView, ReservaUpdateView, ReservaDeleteView,
    
    # Vistas de Agente
    AgenteListView, AgenteCreateView, AgenteUpdateView, AgenteDeleteView
)

urlpatterns = [
    # URL para la página de inicio
    path('', HomeView.as_view(), name='home'),

    # URLs para Destino
    path('destinos/', DestinoListView.as_view(), name='ver_destinos'),
    path('destinos/agregar/', DestinoCreateView.as_view(), name='agregar_destino'),
    path('destinos/actualizar/<int:pk>/', DestinoUpdateView.as_view(), name='actualizar_destino'),
    path('destinos/eliminar/<int:pk>/', DestinoDeleteView.as_view(), name='eliminar_destino'),

    # URLs para Vuelo
    path('vuelos/', VueloListView.as_view(), name='ver_vuelos'),
    path('vuelos/agregar/', VueloCreateView.as_view(), name='agregar_vuelo'),
    path('vuelos/actualizar/<int:pk>/', VueloUpdateView.as_view(), name='actualizar_vuelo'),
    path('vuelos/eliminar/<int:pk>/', VueloDeleteView.as_view(), name='eliminar_vuelo'),

    # URLs para Alojamiento
    path('alojamientos/', AlojamientoListView.as_view(), name='ver_alojamientos'),
    path('alojamientos/agregar/', AlojamientoCreateView.as_view(), name='agregar_alojamiento'),
    path('alojamientos/actualizar/<int:pk>/', AlojamientoUpdateView.as_view(), name='actualizar_alojamiento'),
    path('alojamientos/eliminar/<int:pk>/', AlojamientoDeleteView.as_view(), name='eliminar_alojamiento'),
    
    # URLs para PaqueteTuristico
    path('paquetes/', PaqueteTuristicoListView.as_view(), name='ver_paquetes_turisticos'),
    path('paquetes/agregar/', PaqueteTuristicoCreateView.as_view(), name='agregar_paquete_turistico'),
    path('paquetes/actualizar/<int:pk>/', PaqueteTuristicoUpdateView.as_view(), name='actualizar_paquete_turistico'),
    path('paquetes/eliminar/<int:pk>/', PaqueteTuristicoDeleteView.as_view(), name='eliminar_paquete_turistico'),
    
    # URLs para Cliente
    path('clientes/', ClienteListView.as_view(), name='ver_clientes'),
    path('clientes/agregar/', ClienteCreateView.as_view(), name='agregar_cliente'),
    path('clientes/actualizar/<int:pk>/', ClienteUpdateView.as_view(), name='actualizar_cliente'),
    path('clientes/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='eliminar_cliente'),
    
    # URLs para Reserva
    path('reservas/', ReservaListView.as_view(), name='ver_reservas'),
    path('reservas/agregar/', ReservaCreateView.as_view(), name='agregar_reserva'),
    path('reservas/actualizar/<int:pk>/', ReservaUpdateView.as_view(), name='actualizar_reserva'),
    path('reservas/eliminar/<int:pk>/', ReservaDeleteView.as_view(), name='eliminar_reserva'),
    
    # URLs para Agente
    path('agentes/', AgenteListView.as_view(), name='ver_agentes'),
    path('agentes/agregar/', AgenteCreateView.as_view(), name='agregar_agente'),
    path('agentes/actualizar/<int:pk>/', AgenteUpdateView.as_view(), name='actualizar_agente'),
    path('agentes/eliminar/<int:pk>/', AgenteDeleteView.as_view(), name='eliminar_agente'),
]
