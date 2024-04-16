#9.	Considerando que el consumo de servicios públicos de un establecimiento ha venido aumentando el alcalde de la ciudad
# requiere de un programa que le permita saber cuánto ha pagado al año y por mes le muestre cuanto paga para poder
# tener un control de su gasto para este concepto.
lista_consumo_servicios = [200,300,400,500,600,700,800,900,800,300,100,200]
suma = 0
z = 0
suma_2 = 0
while z<= len(lista_consumo_servicios) + 1:
     suma = suma + lista_consumo_servicios[z]
     z += 1
     suma_2 += lista_consumo_servicios[z]
     print(suma_2)
print ("Los elementos de la consumo mensual son:")
print (lista_consumo_servicios)
print (f"Durante el año ha pagado por concepto de servicios el siguiente valor: {suma}")



#for z in lista_consumo_servicios:
    #if z > 0:
     #print (f"el consumo mensual es de: {z}")
