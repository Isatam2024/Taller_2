#Se desea conocer para un grupo de 10 personas, el total de personas por rango de edades.
# Los rangos son los siguientes: 0-20, 20-30,30,40, 40-60 y mayores de 60.
# Elabore un algoritmo y la prueba de escritorio que permita mostrar los totales respectivos.
cant_personas = 10
contador_0_20 = 0
contador_20_30 = 0
contador_30_40 = 0
contador_40_60 = 0
contador_mas_60 = 0

for cont in range(cant_personas):
    print ("Ingrese la edad #" ,(cont+1))
    edad = int(input())
    if edad <= 20:
        contador_0_20 += 1
    elif edad <= 30:
        contador_20_30 += 1
    elif edad >30:
        contador_30_40 += 1
    elif edad >= 40:
        contador_40_60 += 1
    elif edad >= 60:
        contador_mas_60 += 1
    else:
        print("Error, ingrese una edad entre 0 y 60")
    print("Total de personas entre 0 y 20:", contador_0_20,"Total de personas entre 30 y 40:", contador_20_30,"  Total de personas entre 40 y 60:", contador_40_60, " Total de personas mayores de 60:", contador_mas_60)





