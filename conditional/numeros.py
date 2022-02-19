"""
escriba una funcion que reciba por parametro un número entero y devuelva:
-1 si el numero es negativo 
0 si el número es positivo pero menor a 1000
1 si el número es positivo y se encuentra entre 1000 y 10000
2 si el número es positivo y es mayor a 10000

@CatherineHerrera96
"""


def numero_analizar (numero: int) -> int:
    s = -1
    if (0 <= numero < 1000):
        s = 0
    elif (1000 <= numero < 10000): 
        s = 1
    elif (numero >= 10000):
        s = 2
    return s

numero = int(input("ingrese el número que quiere analizar:"))

analizar = numero_analizar(numero)
print (analizar)