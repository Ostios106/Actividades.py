def calcular_descuento_traje(precio):
    if precio > 2500:
        descuento = precio * 0.15
    else:
        descuento = precio * 0.08
    precio_final = precio - descuento
    return descuento, precio_final

# Ejemplo de uso
precio = float(input("Ingrese el precio del traje: "))
descuento, precio_final = calcular_descuento_traje(precio)
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Precio final a pagar: ${precio_final:.2f}")
