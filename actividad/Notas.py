
print("--- Calculadora de Promedio de Notas ---")
print("Ingrese las cuatro notas (pueden ser decimales):")

C1 = float(input("Ingrese la primera nota: "))
C2 = float(input("Ingrese la segunda nota: "))
C3 = float(input("Ingrese la tercera nota: "))
C4 = float(input("Ingrese la cuarta nota: "))

#Calcular el promedio
promedio = (C1 + C2 + C3 + C4) / 4

#Mostrar los resultados
print("\n=== Resultados ===")
print(f"Nota 1: {C1}")
print(f"Nota 2: {C2}")
print(f"Nota 3: {C3}")
print(f"Nota 4: {C4}")
print(f"Promedio: {promedio:.2f}")

