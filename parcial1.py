#1. Escribe un programa que reciba un número entero y determine si es primo o no, mostrando un mensaje apropiado.
#hecho por Jesús Miranda
num = int(input("ingrese un numero entero: "))
if num < 0:
    print("ingrese un valor positivo")
else:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
    if primo:
        print("el numero es primo")
        
        

#2. Crea un programa que pida una cadena al usuario y cuente cuántas vocales contiene (sin importar mayúsculas o minúsculas). 
#hecho por Julio Ahumada
cadena = input("Introduce una cadena de texto: ")
contador_vocales = 0
vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "ü", "A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú", "Ü"]
for caracter in cadena:
  if caracter in vocales:
    contador_vocales += 1
print("El número de vocales en la cadena es: ",contador_vocales)