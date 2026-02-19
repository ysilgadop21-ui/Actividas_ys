# ==============================
# SMART DELIVERY (datos estáticos)
# ==============================

# ---- Función cálculo de tarifa por zona ----
def calcular_tarifa(zona):
    tarifas = {
        "Torices": 15000,
        "Marbella": 10000,
        "Bicentenario": 70000
    }
    return tarifas.get(zona, 0)


# ---- Función asignar repartidor ----
def asignar_repartidor(zona):
    repartidores = {
        "Torices": "Roy",
        "Marbella": "Luis",
        "Bicentenario": "Diana"
    }
    return repartidores.get(zona, "Disponible")


# ---- Registro de pedido (datos estáticos) ----
def registrar_pedido():
    pedido = {
        "cliente": "Ana Gómez",
        "direccion": "Carrera 5 #12-30",
        "telefono": "3019876543",
        "zona": "Torices",
        "producto": "Documento urgente"
    }
    return pedido


# ---- Gestión completa del envío ----
def gestionar_envio():

    pedido = registrar_pedido()

    tarifa = calcular_tarifa(pedido["zona"])
    repartidor = asignar_repartidor(pedido["zona"])

    print("===== SMART DELIVERY =====")
    print("Cliente:", pedido["cliente"])
    print("Dirección:", pedido["direccion"])
    print("Teléfono:", pedido["telefono"])
    print("Zona:", pedido["zona"])
    print("Producto:", pedido["producto"])
    print("Repartidor:", repartidor)
    print("Costo del envío: $", tarifa)
    print("===========================")


# ---- Ejecutar sistema ----
gestionar_envio()

