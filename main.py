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

#Creamos la función lee_numero, dentro de la fución, le diremos al usuario que introduzca tres números que se imprimirán por pantalla en una tabla. Dentro de la función número crearemos una función llamada "mayor" que nos buscará el numero mayor de los tres introducidos. Para ellos usaremos dos condicionales que nos parametrizan la función. Por último, imprimiremos por pantalla el numero mayor.
def lee_numero():
  print("Introduce tres números diferentes\n")
  num1=float(input("Introduzca el primer número: "))
  num2=float(input("Introduzca el segundo número: "))
  num3=float(input("Introduzca el tercer número: "))
  lista=[num1, num2, num3]
  print(lista)
  print("\n")
  def mayor():
    if num1>num2 and num1>num3:
      num_mayor=num1
    elif num2>num1 and num2>num3:
      num_mayor=num2
    elif num3>num1 and num3>num2:
      num_mayor=num3
    elif num1==num2==num3:
      print("ERROR")
      
    print("El número más grande es: ", num_mayor)
    return mayor
  mayor()

lee_numero()



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
  