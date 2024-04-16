#1.	Elabore un programa que permita mostrar el sueldo promedio de un grupo de empleados

sueldo_empleados=[1400,1900,2000]
aux=0
for e in range(0,3):
  aux=sueldo_empleados[e]+aux
print(f"El sueldo promedio del grupo de empleados es: {aux/3}")