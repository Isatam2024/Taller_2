#Pide al usuario que ingrese una palabra o frase y usa un ciclo for para contar cuántas vocales
# (a, e, i, o, u) contiene.  Luego, muestra el conteo de cada vocal por separado.
contador=0
palabra= input(f"Ingrese la palabra:")  # str(input("Ingresa la palabra:"))
lista_vocales=['a','e','i','o','u']
for i in palabra:
  if i in lista_vocales:
    contador+=1
print(f"Contiene {contador} vocales")