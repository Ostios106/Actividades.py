def calcular_pago_frutas(monto):
    if monto > 200:
        descuento = monto * 0.10
    elif monto > 100:
        descuento = monto * 0.05
    else:
        descuento = 0
    total_pagar = monto - descuento
    return descuento, total_pagar

# Ejemplo de uso
monto = float(input("Ingrese el monto de la compra en frutas: "))
descuento, total = calcular_pago_frutas(monto)
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${total:.2f}")
