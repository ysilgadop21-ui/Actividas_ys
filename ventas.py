def analizar_ventas(ventas):
    mayor = max(ventas)
    menor = min(ventas)
    promedio = sum(ventas) / len(ventas)
    return mayor, menor, promedio


# Datos dados en el ejercicio
ventas = [2380, 720, 1347, 4600, 1320, 220]

# Prueba
mayor, menor, promedio = analizar_ventas(ventas)

print("\nVenta mayor:", mayor)
print("Venta menor:", menor)
print("Promedio de ventas:", promedio)