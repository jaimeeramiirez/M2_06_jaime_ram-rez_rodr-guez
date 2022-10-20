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


#EJERCICIO 2
print("\n\n")

#Creamos la función lee_numero, dentro de la fución. Dentro de la función número crearemos una función llamada "mayor" que nos buscará el numero mayor de los tres introducidos; los número los introduciremos con la función mayor y buscará el número MÁXIMO con la función MAX.
def lee_numero():
  num=float(input("Introduzca un número: "))
  return num
def mayor():
    num1= lee_numero()
    num2= lee_numero()
    num3= lee_numero()
    MAX=max(num1, num2, num3)
    print("El número más grande es: ", MAX)
    return mayor

mayor()





#EJERCICIO 3
print("\n\n")

#Creamos la función imc, que nos calculará el índice de masa corporal. Utilizaremos la variables peso y altura para almacenar los datos y la fórmula del IMC para obtener un valor. Este valor se comprarará mediante condicionales para ver si el usuario está sano o tiene algun trastorno en su peso corporal. Por último, imprimeros por pantalla el diagnóstico.
def imc():
  print("Vamos a calcular tu IMC o índice de masa corporal: ")
  peso=int(input("Cuál es tu peso en kg? "))
  altura= float(input("Cúal es tu altura en metros?\nPara la altura debes introducir dos decimales: "))
  IMC= peso/(altura*altura)
  print("Tu indice de masa corporal es de: ",IMC)
  if (25.00<=IMC<=30.00):
    print("Por lo tanto, tienes sobrepreso")
  elif (IMC>=30.00):
    print("Por lo tanto, tienes obesidad")
  elif (IMC<18.50):
    print("Por lo tanto, pesas demasiado poco")
  else:
    print("Por lo tanto, tu peso es normal")

  return imc
imc()
  