#Escriba una función en python que pida un número entero positivo y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves. 
n = int(input("ingrese un numero entero posotivo: "))
diccionario_cuadrados = {}
for i in range(1, n + 1):
      diccionario_cuadrados[i] = i ** 2
print("Diccionario de cuadrados:", diccionario_cuadrados)


#Escribe una función que reciba como parámetro una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.
cadena = input("ingrese una cadena de texto: ")
diccionario_cadenas = {}
for caracter in cadena:
    if caracter in diccionario_cadenas:
        diccionario_cadenas[caracter] += 1
    else:
        diccionario_cadenas[caracter] = 1
print("Apareciones de caracteres: ", diccionario_cadenas)