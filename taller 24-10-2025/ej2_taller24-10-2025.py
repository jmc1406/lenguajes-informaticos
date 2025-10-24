cadena = input("ingrese una cadena de texto: ")
diccionario_cadenas = {}
for caracter in cadena:
    if caracter in diccionario_cadenas:
        diccionario_cadenas[caracter] += 1
    else:
        diccionario_cadenas[caracter] = 1
print("Apareciones de caracteres: ", diccionario_cadenas)
