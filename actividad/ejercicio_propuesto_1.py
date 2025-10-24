import math

def calcular_area_figura(H, R):
    # Calcular el cateto faltante usando Pitágoras
    cateto_faltante = math.sqrt(H**2 - R**2)

    # Área de un triángulo rectángulo
    area_triangulo = (R * cateto_faltante) / 2

    # Área total de los dos triángulos
    area_total_triangulos = 2 * area_triangulo

    # Área de la semicircunferencia
    area_semicirculo = (math.pi * R**2) / 2

    # Área total
    area_total = area_total_triangulos + area_semicirculo
    return area_total

# Ejemplo de uso
H = float(input("Ingrese la hipotenusa en metros: "))
R = float(input("Ingrese el cateto (también radio) en metros: "))

area = calcular_area_figura(H, R)
print(f"El área total de la figura es: {area:.2f} metros cuadrados")
