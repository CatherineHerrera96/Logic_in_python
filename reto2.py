a = input("ingrese la lista de favoritos de Pedro: ")
b = input("ingrese la lista de favoritos de Jimena: ")
c = input("ingresa la lista de ganadores: ")

lista = ""

P = 0
J = 0 

for A in c:
  if A in a:
    P += 1
  if A in b :
    J += 1
  if J > P:
    lista = lista + "J"
  if P > J:
    lista = lista + "P"
  if P == J:
    lista = lista + "E"


print (lista)