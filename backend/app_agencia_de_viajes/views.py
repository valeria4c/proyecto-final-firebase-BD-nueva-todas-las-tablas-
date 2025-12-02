
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Destino, Vuelo, Alojamiento, Paquete_Turistico, Cliente_Viajes, Reserva_Viaje, Agente_Viajes
from .forms import (
    DestinoForm, VueloForm, AlojamientoForm, PaqueteTuristicoForm, 
    ClienteViajesForm, ReservaViajeForm, AgenteViajesForm
)

# ==========================================
# VISTAS DE LA PÁGINA DE INICIO
# ==========================================
class HomeView(View):
    def get(self, request):
        return render(request, 'app_agencia_de_viajes/home.html')

# ==========================================
# VISTAS PARA Destino
# ==========================================
class DestinoListView(View):
    def get(self, request):
        destinos = Destino.objects.all()
        return render(request, 'app_agencia_de_viajes/destino/ver.html', {'destinos': destinos})

class DestinoCreateView(View):
    def get(self, request):
        form = DestinoForm()
        return render(request, 'app_agencia_de_viajes/destino/agregar.html', {'form': form})

    def post(self, request):
        form = DestinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_destinos')
        return render(request, 'app_agencia_de_viajes/destino/agregar.html', {'form': form})

class DestinoUpdateView(View):
    def get(self, request, pk):
        destino = get_object_or_404(Destino, pk=pk)
        form = DestinoForm(instance=destino)
        return render(request, 'app_agencia_de_viajes/destino/actualizar.html', {'form': form})

    def post(self, request, pk):
        destino = get_object_or_404(Destino, pk=pk)
        form = DestinoForm(request.POST, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('ver_destinos')
        return render(request, 'app_agencia_de_viajes/destino/actualizar.html', {'form': form})

class DestinoDeleteView(View):
    def get(self, request, pk):
        destino = get_object_or_404(Destino, pk=pk)
        return render(request, 'app_agencia_de_viajes/destino/eliminar.html', {'destino': destino})

    def post(self, request, pk):
        destino = get_object_or_404(Destino, pk=pk)
        destino.delete()
        return redirect('ver_destinos')

# ==========================================
# VISTAS PARA Vuelo
# ==========================================
class VueloListView(View):
    def get(self, request):
        vuelos = Vuelo.objects.all()
        return render(request, 'app_agencia_de_viajes/vuelo/ver.html', {'vuelos': vuelos})

class VueloCreateView(View):
    def get(self, request):
        form = VueloForm()
        return render(request, 'app_agencia_de_viajes/vuelo/agregar.html', {'form': form})

    def post(self, request):
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_vuelos')
        return render(request, 'app_agencia_de_viajes/vuelo/agregar.html', {'form': form})

class VueloUpdateView(View):
    def get(self, request, pk):
        vuelo = get_object_or_404(Vuelo, pk=pk)
        form = VueloForm(instance=vuelo)
        return render(request, 'app_agencia_de_viajes/vuelo/actualizar.html', {'form': form})

    def post(self, request, pk):
        vuelo = get_object_or_404(Vuelo, pk=pk)
        form = VueloForm(request.POST, instance=vuelo)
        if form.is_valid():
            form.save()
            return redirect('ver_vuelos')
        return render(request, 'app_agencia_de_viajes/vuelo/actualizar.html', {'form': form})

class VueloDeleteView(View):
    def get(self, request, pk):
        vuelo = get_object_or_404(Vuelo, pk=pk)
        return render(request, 'app_agencia_de_viajes/vuelo/eliminar.html', {'vuelo': vuelo})

    def post(self, request, pk):
        vuelo = get_object_or_404(Vuelo, pk=pk)
        vuelo.delete()
        return redirect('ver_vuelos')

# ==========================================
# VISTAS PARA Alojamiento
# ==========================================
class AlojamientoListView(View):
    def get(self, request):
        alojamientos = Alojamiento.objects.all()
        return render(request, 'app_agencia_de_viajes/alojamiento/ver.html', {'alojamientos': alojamientos})

class AlojamientoCreateView(View):
    def get(self, request):
        form = AlojamientoForm()
        return render(request, 'app_agencia_de_viajes/alojamiento/agregar.html', {'form': form})

    def post(self, request):
        form = AlojamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_alojamientos')
        return render(request, 'app_agencia_de_viajes/alojamiento/agregar.html', {'form': form})

class AlojamientoUpdateView(View):
    def get(self, request, pk):
        alojamiento = get_object_or_404(Alojamiento, pk=pk)
        form = AlojamientoForm(instance=alojamiento)
        return render(request, 'app_agencia_de_viajes/alojamiento/actualizar.html', {'form': form})

    def post(self, request, pk):
        alojamiento = get_object_or_404(Alojamiento, pk=pk)
        form = AlojamientoForm(request.POST, instance=alojamiento)
        if form.is_valid():
            form.save()
            return redirect('ver_alojamientos')
        return render(request, 'app_agencia_de_viajes/alojamiento/actualizar.html', {'form': form})

class AlojamientoDeleteView(View):
    def get(self, request, pk):
        alojamiento = get_object_or_404(Alojamiento, pk=pk)
        return render(request, 'app_agencia_de_viajes/alojamiento/eliminar.html', {'alojamiento': alojamiento})

    def post(self, request, pk):
        alojamiento = get_object_or_404(Alojamiento, pk=pk)
        alojamiento.delete()
        return redirect('ver_alojamientos')

# ==========================================
# VISTAS PARA PaqueteTuristico
# ==========================================
class PaqueteTuristicoListView(View):
    def get(self, request):
        paquetes = Paquete_Turistico.objects.all()
        return render(request, 'app_agencia_de_viajes/paquete_turistico/ver.html', {'paquetes': paquetes})

class PaqueteTuristicoCreateView(View):
    def get(self, request):
        form = PaqueteTuristicoForm()
        return render(request, 'app_agencia_de_viajes/paquete_turistico/agregar.html', {'form': form})

    def post(self, request):
        form = PaqueteTuristicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_paquetes_turisticos')
        return render(request, 'app_agencia_de_viajes/paquete_turistico/agregar.html', {'form': form})

class PaqueteTuristicoUpdateView(View):
    def get(self, request, pk):
        paquete = get_object_or_404(Paquete_Turistico, pk=pk)
        form = PaqueteTuristicoForm(instance=paquete)
        return render(request, 'app_agencia_de_viajes/paquete_turistico/actualizar.html', {'form': form})

    def post(self, request, pk):
        paquete = get_object_or_404(Paquete_Turistico, pk=pk)
        form = PaqueteTuristicoForm(request.POST, instance=paquete)
        if form.is_valid():
            form.save()
            return redirect('ver_paquetes_turisticos')
        return render(request, 'app_agencia_de_viajes/paquete_turistico/actualizar.html', {'form': form})

class PaqueteTuristicoDeleteView(View):
    def get(self, request, pk):
        paquete = get_object_or_404(Paquete_Turistico, pk=pk)
        return render(request, 'app_agencia_de_viajes/paquete_turistico/eliminar.html', {'paquete': paquete})

    def post(self, request, pk):
        paquete = get_object_or_404(Paquete_Turistico, pk=pk)
        paquete.delete()
        return redirect('ver_paquetes_turisticos')

# ==========================================
# VISTAS PARA Cliente
# ==========================================
class ClienteListView(View):
    def get(self, request):
        clientes = Cliente_Viajes.objects.all()
        return render(request, 'app_agencia_de_viajes/cliente/ver.html', {'clientes': clientes})

class ClienteCreateView(View):
    def get(self, request):
        form = ClienteViajesForm()
        return render(request, 'app_agencia_de_viajes/cliente/agregar.html', {'form': form})

    def post(self, request):
        form = ClienteViajesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes')
        return render(request, 'app_agencia_de_viajes/cliente/agregar.html', {'form': form})

class ClienteUpdateView(View):
    def get(self, request, pk):
        cliente = get_object_or_404(Cliente_Viajes, pk=pk)
        form = ClienteViajesForm(instance=cliente)
        return render(request, 'app_agencia_de_viajes/cliente/actualizar.html', {'form': form})

    def post(self, request, pk):
        cliente = get_object_or_404(Cliente_Viajes, pk=pk)
        form = ClienteViajesForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes')
        return render(request, 'app_agencia_de_viajes/cliente/actualizar.html', {'form': form})

class ClienteDeleteView(View):
    def get(self, request, pk):
        cliente = get_object_or_404(Cliente_Viajes, pk=pk)
        return render(request, 'app_agencia_de_viajes/cliente/eliminar.html', {'cliente': cliente})

    def post(self, request, pk):
        cliente = get_object_or_404(Cliente_Viajes, pk=pk)
        cliente.delete()
        return redirect('ver_clientes')

# ==========================================
# VISTAS PARA Reserva
# ==========================================
class ReservaListView(View):
    def get(self, request):
        reservas = Reserva_Viaje.objects.all()
        return render(request, 'app_agencia_de_viajes/reserva/ver.html', {'reservas': reservas})

class ReservaCreateView(View):
    def get(self, request):
        form = ReservaViajeForm()
        return render(request, 'app_agencia_de_viajes/reserva/agregar.html', {'form': form})

    def post(self, request):
        form = ReservaViajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_reservas')
        return render(request, 'app_agencia_de_viajes/reserva/agregar.html', {'form': form})

class ReservaUpdateView(View):
    def get(self, request, pk):
        reserva = get_object_or_404(Reserva_Viaje, pk=pk)
        form = ReservaViajeForm(instance=reserva)
        return render(request, 'app_agencia_de_viajes/reserva/actualizar.html', {'form': form})

    def post(self, request, pk):
        reserva = get_object_or_404(Reserva_Viaje, pk=pk)
        form = ReservaViajeForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('ver_reservas')
        return render(request, 'app_agencia_de_viajes/reserva/actualizar.html', {'form': form})

class ReservaDeleteView(View):
    def get(self, request, pk):
        reserva = get_object_or_404(Reserva_Viaje, pk=pk)
        return render(request, 'app_agencia_de_viajes/reserva/eliminar.html', {'reserva': reserva})

    def post(self, request, pk):
        reserva = get_object_or_404(Reserva_Viaje, pk=pk)
        reserva.delete()
        return redirect('ver_reservas')

# ==========================================
# VISTAS PARA Agente
# ==========================================
class AgenteListView(View):
    def get(self, request):
        agentes = Agente_Viajes.objects.all()
        return render(request, 'app_agencia_de_viajes/agente/ver.html', {'agentes': agentes})

class AgenteCreateView(View):
    def get(self, request):
        form = AgenteViajesForm()
        return render(request, 'app_agencia_de_viajes/agente/agregar.html', {'form': form})

    def post(self, request):
        form = AgenteViajesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_agentes')
        return render(request, 'app_agencia_de_viajes/agente/agregar.html', {'form': form})

class AgenteUpdateView(View):
    def get(self, request, pk):
        agente = get_object_or_404(Agente_Viajes, pk=pk)
        form = AgenteViajesForm(instance=agente)
        return render(request, 'app_agencia_de_viajes/agente/actualizar.html', {'form': form})

    def post(self, request, pk):
        agente = get_object_or_404(Agente_Viajes, pk=pk)
        form = AgenteViajesForm(request.POST, instance=agente)
        if form.is_valid():
            form.save()
            return redirect('ver_agentes')
        return render(request, 'app_agencia_de_viajes/agente/actualizar.html', {'form': form})

class AgenteDeleteView(View):
    def get(self, request, pk):
        agente = get_object_or_404(Agente_Viajes, pk=pk)
        return render(request, 'app_agencia_de_viajes/agente/eliminar.html', {'agente': agente})

    def post(self, request, pk):
        agente = get_object_or_404(Agente_Viajes, pk=pk)
        agente.delete()
        return redirect('ver_agentes')
