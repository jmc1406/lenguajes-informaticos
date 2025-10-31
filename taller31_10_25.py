#gurpo: Jesus Miranda, Edwin Diazgranados, Luis loaiza
#Ejercicio 1
Frutas = ["manzana", "banano", "pera", "uva", "naranja"]
 
primer_elemento = Frutas[0]
print("Primer elemento:", primer_elemento)
 
ultimo_elemento = Frutas[-1]
print("ultimo elemento:", ultimo_elemento)
 
Frutas.append("Mango")
 
Frutas.remove("pera")
print("Lista despues de eliminar la fruta:", Frutas)

#ejrcicio 2
numeros = [1,2,3,4,5,6,7,8,9,10]
suma_total = sum(numeros)
mayor = max(numeros)
menor = min(numeros)
promedio = suma_total / len(numeros)
print("suma total de la lista: ", suma_total)
print("numero mas grande de la lista: ", mayor)
print("numero mas pequeño de la lista: ", menor)
print("promedio  de la lista: ", promedio)

#Ejercico 3
nombres = ["Ana", "Luis", "Sofia", "Pedro", "Carla"]
for i in range(len(nombres)):
    print("Nombre numero ", i + 1, ": ", nombres[i])
for i in range(len(nombres)):
    if len(nombres[i]) > 4:
        print("Nombre con más de 4 letras: ", nombres[i])
 
#Ejercicio 4
edades = [12, 17, 18, 20, 15, 22, 13]
mayores_de_edad = []
for edad in edades:
    if edad >= 18:
        mayores_de_edad.append(edad)
print("Numero de edades mayores o iguales a 18 : ", len(mayores_de_edad), "\nEdades: ", mayores_de_edad)


#ejercicio 5
notas = [4.5, 3.5, 4.9, 3.1, 4.6]
promdio_notas = sum(notas)/ len(notas)
if promdio_notas >= 3.0:
    print("el promedio es aprobado: ", promdio_notas)
else: 
    print("el promedio es reprobado: ",promdio_notas )    
notas.sort()
print("notas ordenadas de menor a myor: ", notas)

#Ejercicio 6

productos = []
precios = []
 
for i in range(5):
    nombre = input(f"Ingrese el nombre del producto {i + 1}: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
   
    productos.append(nombre)
    precios.append(precio)
 
total = sum(precios)
 
precio_max = max(precios)
precio_min = min(precios)
 
producto_mas_caro = productos[precios.index(precio_max)]
producto_mas_barato = productos[precios.index(precio_min)]
 
print("\n--- RESULTADOS ---")
print("Lista de productos:", productos)
print("Lista de precios:", precios)
print("Precio total de todos los productos: $", total)
print("Producto más caro:", producto_mas_caro, "($", precio_max, ")")
print("Producto más barato:", producto_mas_barato, "($", precio_min, ")")