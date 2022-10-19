#EJERCICIO 1
print("\n")
import math
print(math.pi)
print("\n")

#Creamos la fución area_circulo, creamos la variable radio con un "float(input..." para poder introducir valores con decimales. Por último usamos la fórmula del área del círculo para resolver el problema.
def area_circulo():
  radio=float(input("Introduce el radio del círculo: "))
  area_circulo=(math.pi*(radio*radio))
  print("El área del círculo es:", area_circulo, "u^2")
  return area_circulo
area_circulo()

