"""
Crea una función que reciba cuatro numeros entrero y retorne el mayor de estos. Si hay dos o mas iguales y mayores, retornara cuanquiera de estos.
Create a feature that receives four entrero numbers and returns the largest of these. If there are two or more equal and larger, return how many of these.

@CatherineHerrera96
"""
def numero_mayor (a:int,b:int,c:int,d:int)-> int:
    if a >= b and c and d:
        print (a)
    elif b >= a and c and d:
        print (b)
    elif c >= a and b and d:
        print (c)   
    elif d >= a and b and c:
        print (d)




a = int(input("ingrese el primer valor: "))
b = int(input("ingrese el segundo valor: "))
c = int(input("ingrese el tercer valor: "))
d = int(input("ingrese el cuarto valor: "))
 

x = numero_mayor(a,b,c,d)
