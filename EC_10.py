#10.Desarrolle un programa que permita saber el salario de 20 empleados por mes se
# requiere el promedio de estos y el pago de cado uno de igual manera cuanto ganaran si se hace un incremento del 2.5%
lista_salario_empleados = [78567, 112345, 46890, 142156, 98216, 55364, 134863, 67892, 122365, 89654, 105216, 43567, 116789, 76543, 138987, 95234, 58678, 128345, 72156, 103456]
suma_salario = 0
aumento_salario = 0.025

for salario in lista_salario_empleados:
    sum_salario =+ salario

promedio = sum_salario/len(lista_salario_empleados)
print (f"El promedio de salario de los 20 empleados es {promedio}")
for x in range(len(lista_salario_empleados)):
     lista_salario_empleados[x] =  lista_salario_empleados[x] * aumento_salario + lista_salario_empleados[x]
print (lista_salario_empleados)



