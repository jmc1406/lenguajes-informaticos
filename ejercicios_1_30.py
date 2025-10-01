#menu 


#ejercicio 1 : escribe un programa que imprima "Hola Mundo"
print("Hola Mundo")

#ejercicio 2: pide el usario su nombre y mestralo en pantalla
nombre = input("ingrese su nombre: ")
print("hola ",nombre)


#ejercicio 3: pide dos numeros al usuario y muestra su suma
num1=int(input("digite un numero: "))
num2=int(input("digite otro numero:"))
suma = num1 + num2
print("la suma de esos numeros es: ", suma)

#ejercico 4: calcula el area de un triangulo
base = int(input("ingrese la base del tringulo: "))
altura = int(input("ingrese la altura del tringulo: "))
area = (base * altura)/ 2
print("el area del tringulo es: ", area)

#ejercicio 5: convierte grados celsius a fahrenheit
grados_c = int(input("ingrese temperatura en °C: "))
grados_f = ((grados_c * 9)/5) + 32
print(" la temperatura en °F es:", grados_f)

#ejercicio 6: pide un numero e imprime si es par o impar
num = int(input("ingrese un numero:"))
if num % 2 == 0:
    print("numero par")
else:
    print("numero impar")
    
#ejercicio 7: pide 3 numero e imprime el mayor
num1 = int(input("ingrese el primer numero:"))
num2 = int(input("ingrese el segundo numero"))
num3 = int(input("ingrese el tercer numero"))
if num1 >= num2 and num1 >= num3:
    print("el numero mayor es:", num1)
elif num2 >= num1 and num2 >= num3:
    print("el numero mayor es: ",num2)
else:
    print("el numero mayor es: ",num3)
    
#ejercicio 8: calcula el cuadrado de un numero
num = int(input("ingrese numero que desea calcular cuadrado:"))
cuadreado = num * num
print("el cuadrado del numero es: ",cuadreado)

#ejercicio 9: pide un numero y muetra su tabla de multiplicar
num = int(input("ingrese valor de la trabla de multipilcar: "))
for i in range(1,11):
    resultado = num * i 
    print(num, "x", i, "=", resultado) 
    
#ejercicio 10: pide una palabra y muestrala al reves
pal = input("ingrese una palabra:")
print("la palabra al reves es: ",pal[::-1])


#ejercico 11: pide la edad y determina si es mayor o menor de edad  
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("es mayor de edad")
else: 
    print("es menor de edad")
    
    
#ejercico 12: calcula el factorial de un numero
num = int(input("ingrese el numero: "))
factorial = 1
for i in range (1, num ):
    factorial = factorial * i
    print("el factorial del numero es:", factorial)

#ejercicio 13: pide 5 numeros y muestra su promedio
num1 = int(input("ingese un numero: "))
num2 = int(input("ingrese otro numero: "))
num3 = int(input("ingrese otro numero: "))
num4 = int(input("ingrese otro numero: "))
num5 = int(input("ingrese otro numero: "))
suma = num1 + num2 + num3 + num4 + num5
prom = suma / 5
print("el promedio de los numero es: ", prom)
    
#ejercico 14: pide un numero y muestra todos los numeros pares desde 1 hasta ese numero
num = int(input("ingrese nu numero: "))
for i in range(1, num + 1):
    if i % 2 == 0:
        print(i, "es numero par")
    else:
        print("no hay numeros pares")
       
#ejercicio 15: pide una letra y determina si es una vocal o consonante
letra = input("ingrese una letra: ")
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if letra in vocales:
    print("es una vocal") 
else:
    print("es una consonante")       
    
    
#ejercicio 16: imprime los primeros 20 numeros de la serie fibonacci
num = 20
a = 0
b = 1
print(a)
print(b)
for i in range(2, num):
    c = a + b
    print(c)
    a = b
    b = c
    
    
#ejrcicio 17: pide un numero y determina si es primo
num = int(input("ingrese un numero:"))
if num < 0:
    print("ingrese un valor positivo")
else:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print("el numero es primo")

#ejercicio 18: genera una lista con numeros del 1 al 100 y muestra los multiplos de 5
    numeros = list(range(1, 101))
    multiplos_de_5 = [n for n in numeros if n % 5 == 0]
    print("Los múltiplos de 5 del 1 al 100 son:", multiplos_de_5)
    
#ejercicio 19: contar vocales en una palabra
palabra = input("ingrese una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
con = 0 
for letra in palabra:
    if letra in vocales:
        con += 1
print("la cantidad de vocales en la palabra es: ", con)


#ejercicio 20: simula una calculadora basica 
num1 = float(input("ingrese el primer numero:"))
num2 = float(input("ingrese el segundo numero:"))
operacion = input("ingrese la operacion : "
                  +"1. suma"
                  +"2. resta"
                  +"3. multiplicacion"
                  +"4. divicion")
if operacion == "suma":
    resultado = num1 + num2
    print("el resultado es: ", resultado)
elif operacion == "resta": 
    resulatdo = num1 - num2 
    print("el resulatdo es: ", resultado)
elif operacion == "multiplicacion":
    resultado = num1 * num2
    print("el resultado es:", resultado)
elif operacion == "divicion":
    if num2 != 0:
        resultado = num1/num2
        print("el resultado es: ", resultado)
    else:
        print("error: no se puede dividir entre cero")
else:
    print("operacion invalida")

#ejercicio 21: crea una lista con 10 numeros y encuentra el mayor
lista = [12, 45, 7, 23, 89, 34, 56, 78, 10, 5]
mayor = max(lista)
print("La lista es:", lista)
print("El número mayor de la lista es:", mayor)


#ejercicio 22: ordena una lista numeros de menor a mayor
lista = [12, 45, 7, 23, 89, 34, 56, 78, 10, 5]
lista_ordenada = sorted(lista)
print("Lista ordenada de menor a mayor:", lista_ordenada)

#ejercicio 23: elimina los duplicados de una lista
lista = [12, 45, 7, 23, 89, 34, 56, 78, 10, 5, 12, 45, 7]
lista_sin_duplicados = list(set(lista))
print("lista sin duplicados:", lista_sin_duplicados)

#ejrcicio 24: crea una lista con nombres y ordenala alfabeticamente
nombres = ["Juan", "Ana", "Pedro", "Maria", "Luis"]
nombres_ordenados = sorted(nombres)
print("nombres ordenados alafbeticamente:", nombres_ordenados)

#ejercicio 25: suma todos los numeros de una lista
numeros = [12, 45, 7, 23, 89, 34, 56, 78, 10, 5]
suma = sum(numeros)
print("la suma de la lista es: ", suma)

#ejercicio 26: une dos listas en una sola
lista1 = [4, 7, 11, 14, 22]
lista2 = [3, 8, 15, 18, 25]
lista_unida = lista1 + lista2
print("lista unida: ", lista_unida)

#ejercicio 27: pide una frase y cuenta cuentas palabras tiene 
frase = input("ingrese una frase: ")
palabras = frase.split()
cantidad_palabras = len(palabras)
print("la cantidad de palabras en la frase es: ", cantidad_palabras)

#ejercicio 28: verifica si una palabra es un palindromo
palabra = input("ingrese una palabra: ")
if palabra == palabra[::-1]:
    print("es un palindromo")
else:
    print("no es un palindromo")
    
#ejercicio 29: crea una lista con los cuadrados de los primeros 10 numeros
cuadrados = [i * i for i in range(1, 11)]
print("los cuadrados son: ", cuadrados)

#ejercicio 30: encuentra el segundo numero mayor en una lista
numeros = [12, 45, 7, 23, 89, 34, 56, 78, 10, 5]
numeros_sin_duplicados = list(set(numeros))
numeros_sin_duplicados.sort()
if len(numeros_sin_duplicados) >= 2:
    segundo_mayor = numeros_sin_duplicados[-2]
    print("el segundo numero mayor es: ", segundo_mayor)

