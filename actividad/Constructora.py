def calcular_area_terreno(A, B, C, h):
    # Área del triángulo
    area_triangulo = (B * h) / 2

    # Base del rectángulo es (A - C)
    base_rectangulo = A - C
    area_rectangulo = base_rectangulo * h

    # Área total
    area_total = area_triangulo + area_rectangulo
    return area_total

# Ejemplo de uso
A = float(input("Ingrese la base total en metros de A: "))
B = float(input("Ingrese la base del triángulo en metros de B: "))
C = float(input("Ingrese la base del rectángulo en metros de C: "))
h = float(input("Ingrese la altura en metros de h: "))

area = calcular_area_terreno(A, B, C, h)
print(f"El área total del terreno es: {area:.2f} metros cuadrados")
