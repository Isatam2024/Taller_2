#Elaborar un algoritmo y su debido proceso de prueba de escritorio que permita obtener
#la factorial de un número.
n = int (input ("Ingresa un número: "))
factorial = 1
if n >= 1:
    for i in range (1, n+1):
        factorial=factorial *i
print("El factorial del numero dado es: ", factorial)