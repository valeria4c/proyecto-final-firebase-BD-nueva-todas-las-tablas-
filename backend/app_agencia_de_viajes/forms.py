from django import forms
from .models import Destino, Paquete_Turistico, Cliente_Viajes, Agente_Viajes, Reserva_Viaje, Vuelo, Alojamiento

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'

class PaqueteTuristicoForm(forms.ModelForm):
    class Meta:
        model = Paquete_Turistico
        fields = '__all__'

class ClienteViajesForm(forms.ModelForm):
    class Meta:
        model = Cliente_Viajes
        fields = '__all__'

class AgenteViajesForm(forms.ModelForm):
    class Meta:
        model = Agente_Viajes
        fields = '__all__'

class ReservaViajeForm(forms.ModelForm):
    class Meta:
        model = Reserva_Viaje
        fields = '__all__'

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = '__all__'

class AlojamientoForm(forms.ModelForm):
    class Meta:
        model = Alojamiento
        fields = '__all__'
