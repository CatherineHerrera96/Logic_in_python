"""
esta es una función mejorada del archivo cuatro_nemeros.py, que reciba cuatro numeros entrero y retorna el mayor de estos. 
Si hay dos o mas iguales y mayores, retornara cuanquiera de estos.

this is an improved function of the cuatro_nemeros.py file, which receives four numbers and returns the largest of these. 
If there are two or more equal and larger, return how many of these.

@CatherineHerrera96
"""

def numero_mayor (a : int, b : int, c : int,  d : int) -> int:
    mayor = a
    if (b > mayor): 
        mayor = b
    if (c > mayor):
        mayor = c 
    if (d > mayor):
        mayor = d
    return mayor

a = int(input("ingrese el primer valor: "))
b = int(input("ingrese el segundo valor: "))
c = int(input("ingrese el tercer valor: "))
d = int(input("ingrese el cuarto valor: "))      

numerom = numero_mayor (a,b,c,d)

print (f"el numero mayor entre {a, b, c, d} es el número {numerom}")