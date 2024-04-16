#2.	Elabore un programa que muestre la
# potencia de 2 de un numero x mientras llegue a 1000
x= int(input("ingrese numero:"))
for i in range(x,10):

  print(i**2)
  x = 1

while x ** 2 < 1000:
  print(x)
  x += 1

  print("¡Bucle completado!")