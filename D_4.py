#4.	Escribe un programa lea una lista de números e imprima la suma de los números pares
lista_numeros=[1,2,3,4,5,6,7,8,9,10]
pares=[]
impares=[]
for i in lista_numeros:
  if i%2==0:
    pares.append(i)
  else:
    impares.append(i)
print(f"los numeros impares son: {impares}")
print(f"los numeros pares son {pares} y su suma es: {sum(pares)}")
