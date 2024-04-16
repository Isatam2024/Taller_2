#3.Elaborar un algoritmo que permita
# las tablas de multiplicar del 1 al 100 de un número ingresado por el usuario. Recuerde realizar la prueba de escritorio.

Numero = int(input("Ingresar el número:"))
multiplicar = 0

for i in range(1, 101):
  if Numero > 0 :
      multiplicar = i*Numero
      print(i, "*",Numero, "=",multiplicar)