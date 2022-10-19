print("\n")
import math
print(math.pi)
print("\n")


def area_cirulo():
  radio=float(input("Introduce el radio del círculo: "))
  area_circulo=(math.pi*(radio*radio))
  print("El área del círculo es:", area_circulo, "u^2")
  return area_cirulo
area_cirulo() 