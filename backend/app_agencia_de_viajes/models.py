from django.db import models

# ==========================================
# MODELO: Destino
# ==========================================
class Destino(models.Model):
    id_destino = models.IntegerField(primary_key=True)
    nombre_destino = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    continente = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    atracciones_principales = models.TextField(blank=True, null=True)
    clima = models.CharField(max_length=50, blank=True, null=True)
    divisa_local = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nombre_destino

# ==========================================
# MODELO: Paquete_Turistico
# ==========================================
class Paquete_Turistico(models.Model):
    id_paquete = models.IntegerField(primary_key=True)
    nombre_paquete = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    precio_adulto = models.DecimalField(max_digits=10, decimal_places=2)
    precio_nino = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cupo_maximo = models.IntegerField()
    incluye_vuelo = models.BooleanField(default=False)
    incluye_alojamiento = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_paquete

# ==========================================
# MODELO: Cliente_Viajes
# ==========================================
class Cliente_Viajes(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateField()
    preferencias_viaje = models.TextField(blank=True, null=True)
    pasaporte = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: Agente_Viajes
# ==========================================
class Agente_Viajes(models.Model):
    id_agente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    dni = models.CharField(max_length=20, unique=True)
    fecha_contratacion = models.DateField()
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    comision_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: Reserva_Viaje
# ==========================================
class Reserva_Viaje(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    id_paquete = models.ForeignKey(Paquete_Turistico, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente_Viajes, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField()
    num_adultos = models.IntegerField()
    num_ninos = models.IntegerField(blank=True, null=True, default=0)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    estado_reserva = models.CharField(max_length=50) # Ej: 'Pendiente', 'Confirmada', 'Cancelada'
    fecha_vencimiento_pago = models.DateField(blank=True, null=True)
    id_agente_venta = models.ForeignKey(Agente_Viajes, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"Reserva {self.id_reserva} - Cliente: {self.id_cliente.nombre} {self.id_cliente.apellido}"

# ==========================================
# MODELO: Vuelo
# ==========================================
class Vuelo(models.Model):
    id_vuelo = models.IntegerField(primary_key=True)
    num_vuelo = models.CharField(max_length=20)
    aerolinea = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()
    fecha_llegada = models.DateField()
    hora_llegada = models.TimeField()
    precio_clase_economica = models.DecimalField(max_digits=10, decimal_places=2)
    asientos_disponibles = models.IntegerField()

    def __str__(self):
        return f"{self.aerolinea} - {self.num_vuelo} ({self.origen} a {self.destino})"

# ==========================================
# MODELO: Alojamiento
# ==========================================
class Alojamiento(models.Model):
    id_alojamiento = models.IntegerField(primary_key=True)
    nombre_hotel = models.CharField(max_length=255)
    tipo_alojamiento = models.CharField(max_length=50, blank=True, null=True) # Ej: 'Hotel', 'Hostal', 'Apartamento'
    direccion = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    estrellas = models.IntegerField(blank=True, null=True)
    precio_noche_estandar = models.DecimalField(max_digits=10, decimal_places=2)
    servicios_incluidos = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre_hotel
