#Aplicación de la estructura MATCH CASE
#Programa que simula el funcionamiento de una calculadora que puede realizar las cuatro operaciones aritméticas básicas
# (suma, resta, producto y división) con valores numéricos enteros. El usuario debe especificar la operación con el primer
# carácter del primer parámetro
# de la línea de comandos: S o s para la suma, R o r para la resta, P, p, M o m
# para el producto y D o d para la división.
# Los valores de los operandos se deben indicar en el segundo y tercer parámetros.

def tienda(tipo_pago, precio, impr):
  iva = 0.19
  match tipo_pago:
        case 'efectivo':
             result = precio * impr
             result_iva = (result * iva) + result
             a = result_iva - (result_iva * 0.1)
             print(f"el total sin descuento es {result_iva}")
             print(f"la forma de pago es {tipo_pago} ")
             print(f"el descuento realizado es 10%")
             print(f"el total  pagar es {a}")
        case 'tarjeta':
             result = precio * impr
             result_iva = (result * iva) + result
             a = result_iva - (result_iva * 0.05)
             print(f"el total sin descuento es {result_iva}")
             print(f"la forma de pago es {tipo_pago} ")
             print(f"el descuento realizado es 5%")
             print(f"el total  pagar es {a}")

        case 'vale':
             result = precio * impr
             result_iva = (result * iva) + result
             a = result_iva - (result_iva * 0.15)
             print(f"el total sin descuento es {result_iva}")
             print(f"la forma de pago es {tipo_pago} ")
             print(f"el descuento realizado es 15%")
             print(f"el total  pagar es {a}")


        case _:
            return "Operador no válido."
print(tienda('efectivo', 80000, 2 ))
print(tienda('tarjeta', 80000, 2 ))
print(tienda('vale', 80000, 2 ))
print(tienda('h', 80000, 2 ))