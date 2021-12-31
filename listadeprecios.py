def sumar_precios (lista_de_precios):
    suma = 0

    for precio in lista_de_precios:
        suma += precio
    
    print (f"la suma de precios es {suma}")

todos_los_precios = [ ]

while True:
    precio = input("ingrese el valor del producto: ")

    if precio == "X":
      break
    
    todos_los_precios.append(int(precio))
    print(todos_los_precios)


sumar_precios(todos_los_precios)

