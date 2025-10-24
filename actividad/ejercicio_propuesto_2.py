def calcular_pago_por_leche(litros, precio_por_galon):
    galones = litros / 3.785
    pago_total = galones * precio_por_galon
    return galones, pago_total

# Ejemplo de uso
litros = float(input("Ingrese la cantidad de litros producidos: "))
precio_por_galon = float(input("Ingrese el precio por galón: "))

galones, pago = calcular_pago_por_leche(litros, precio_por_galon)
print(f"Cantidad en galones: {galones:.2f}")
print(f"Pago total: ${pago:.2f}")
