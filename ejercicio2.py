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
