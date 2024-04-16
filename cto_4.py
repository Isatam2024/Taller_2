#4.	Realice un programa que permita saber el costo total de 10 producto cualquiera y que al final muestre el
# precio antes IVA y el precio después de IVA de la compra
productos = [10,20,25,30,35, 40,50,75,80,100]
sum_prod_sin_iva = 0
sum_prod_con_iva = 0


for producto in productos:
        sum_prod_sin_iva = sum_prod_sin_iva+ producto
        sum_prod_con_iva = sum_prod_sin_iva + 0.19* sum_prod_sin_iva
print (f"El costo total de los productos sin iva es: {sum_prod_sin_iva}")
print (f"El costo total de los productos con iva es: {sum_prod_con_iva}")

