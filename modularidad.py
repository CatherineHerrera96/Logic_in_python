"""
Escriba una función que reciba dos números enteros n y d y determine si n es divisible por 2d (retorna 2),
si n es divisible por d pero no entre 2d (retorna 1) , o si n no es divisible ni por d ni por 2d (retorna 0).

Type a function that receives two integers n and d and determines whether n is divisible by 2d (returns 2),
if n is divisible by d but not by 2d (returns 1) , or if n is not divisible by either d or 2d (returns 0).

@CatherineHerrera96
"""

def es_divisible (n : int, d : int) -> int:
    if ((n % (2*d)) == 0) :
        return 2
    if ((n % d) == 0) :
        return 1
    else:
        return 0 

n = int(input("ingrese n:"))
d = int(input("ingrese d:"))

divisible = es_divisible(n,d)
print (divisible)


