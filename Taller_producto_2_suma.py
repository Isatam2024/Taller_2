#Crea un programa que genere dos números al azar entre el 0 y el 100, y pida al usuario que calcule e introduzca su suma.
# Si la respuesta no es correcta, deberá volver a pedirla tantas veces como sea necesario
# hasta que el usuario acierte. Pista: como verás en el apartado 10, para generar un número al azar
# del 0 al 100 puedes hacer número <- RANDOM (101).
import random
Num_1 = random.randint(0,100)
Num_2 = random.randint(0,100)
Suma_correct = Num_1 + Num_2
Suma_usuario = int(input(f"¿Cuánto es la suma de el {Num_1} y el {Num_2}?:"))

while True:
    if Suma_usuario == Suma_correct:
        print("Has acertado")
        break
    else:
        print("Has fallado")
        Suma_usuario = int(input(f"¿Cuánto es la suma de el {Num_1} y el {Num_2}"))



