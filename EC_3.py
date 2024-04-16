#Elaborar un programa que permita ingresar 10 letras y luego nos indique
# al final cuantas vocales y consonantes se ingresaron
s=[]
contador=0
contador_v=0
contador_c=0
while contador<10:
  s.append(input('ingrese una letra'))
  contador+=1
print(s)
print(s)
lista_vocales=['a','e','i','o','u']
for j in s:
  if j in lista_vocales:
    print(f"{j} es vocal")
    contador_v+=1

  else:
    print(f"{j} es consonanate")
    contador_c+=1
print(f"el total de consonates es {contador_c}")
print(f"el total de vocales es {contador_v}")