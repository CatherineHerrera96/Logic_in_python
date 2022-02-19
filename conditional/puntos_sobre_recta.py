"""
funcion que recibe tre puntos (cordenadas x,y) y determine si estos estan sobre una recta o no. 

function that receives three points (strings x,y) and determines if these are on a line or not.

@CatherineHerrera96
"""


def puntos_sobre_recta (x1 : int, y1 : int, x2 : int, y2 : int, x3 : int, y3 : int) -> bool:
    pendiente1 = (y2 - y1)/(x2 - x1)
    pendiente2 = (y3 - y2)/(x3 - x2)


    if pendiente1 == pendiente2:
        return ("los puntos ingresados son colineales")
    else:
        return ("los puntos ingresados no son colineales")

x1 = int(input("ingrese x1:"))
y1 = int(input("ingrese y1:"))
x2 = int(input("ingrese x2:"))
y2 = int(input("ingrese y2:"))
x3 = int(input("ingrese x3:"))
y3 = int(input("ingrese y3:"))

colineales = puntos_sobre_recta(x1, y1, x2, y2, x3, y3)

print (colineales)