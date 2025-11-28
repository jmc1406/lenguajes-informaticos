from pandas import Series, DataFrame
import numpy as np
import random
lista_aleatoria = [random.randint(1, 100) for _ in range(10)]
print("Lista aleatoria:", lista_aleatoria)

serie_aleatoria = Series(lista_aleatoria, index=range(1, 11))
print("Serie aleatoria:")

serie_aleatoria.name = "numeros_aleatorios"
print(serie_aleatoria)

serie_aleatoria.index.name = "idx"
print(serie_aleatoria)

serie_cuadrados = serie_aleatoria ** 2
print("Serie de cuadrados:")
print(serie_cuadrados)
df = DataFrame(serie_aleatoria)
print("DataFrame de la serie aleatoria:")
print(df)

print("Ultimos 4 elementos de la serie:")
print(serie_aleatoria.tail(4))

numeros_mayores_500 = serie_cuadrados[serie_cuadrados > 500].tolist()
print("Números mayores a 500:", numeros_mayores_500)
