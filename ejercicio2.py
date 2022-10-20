#EJERCICIO 2
print("\n\n")

#Creamos la función lee_numero con la varibale "num" que nos pedirá que introduzcamos un número. Las funciones las utilizamos para ordenar y ahorrar código por lo que con esta función en vez de escribir tres veces: num=float(input("Introduzca un número: ")) solo tendremos que hacer referencia a la función en la otra función que llamaremos "mayor". Esta función buscará el numero mayor de los tres introducidos; para ellor usaremos la herramienta MAX.
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
