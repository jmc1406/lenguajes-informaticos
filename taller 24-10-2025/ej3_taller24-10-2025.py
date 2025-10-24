frutas_precios = {
    "Manzana": 2500,
    "Banana": 500,
    "Pera": 1800,
    "Uva": 4500,
    "Sandia": 5000
}
fruta = input("Digite la fruta que desea comprar: ")
if fruta in frutas_precios:
    cantidad = int(input("Digite la cantidad de frutas a comprar: "))
    precio = frutas_precios[fruta]
    total = precio * cantidad
    print(f"{fruta}: {precio}\nTotal a pagar: {total}")
else:
    print("la fruta no existe")
 
