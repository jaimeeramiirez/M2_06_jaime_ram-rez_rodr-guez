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
  