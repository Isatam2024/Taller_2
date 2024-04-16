#3.	Escribe un programa que lea una lista de palabras
# e imprima la lista de palabras que comiencen con una determinada letra.
Lista_palabras = ["Amor", "Paz", "Vida", "Solidaridad", "Temor", "Sabiduría", "Felicidad", "Esperanza", "Alegría", "Amistad"]
for palabra in Lista_palabras:
    if palabra[0] == "A":
      print(palabra)