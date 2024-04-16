#Crear un programa que pida al usuario una contraseña, de forma repetitiva mientras que no introduzca "1234".
# Cuando finalmente escriba la contraseña correcta, se le dirá "Bienvenido" y terminará el programa.

clave_correcta = 1234

contraseña = int(input("Ingresar la contraseña:"))
while contraseña != clave_correcta:
  print(f"Contraseña incorrecta, intenta otra vez")
  contraseña = int(input("ingrese contraseña:"))


if contraseña == clave_correcta :
  print(f"Bienvenido")