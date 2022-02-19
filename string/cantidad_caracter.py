"""
Nos piden crear una función que nos retorne la cadena con mayor número de "a" entre cuatro cadenas de caracteres. 
Tenemos que tener presente que debemos contar todas las letras a independiente de si están en mayúscula o minúscula y 
que en caso de que varias cadenas tengan la cantidad mayor de a, debemos retornar la primera de estas.

They ask us to create a function that returns the string with the highest number of "a" between four strings of characters.
We have to keep in mind that we must count all the letters a regardless of whether they are uppercase or lowercase and
that in case several chains have the largest amount of a, we must return the first of these.
@CatherineHerrera96
"""

def cadena_mas (cadena1 : str, cadena2 : str, cadena3 : str, cadena4 : str)-> str:
    letra = "a"
    con_mas_a = cadena1
    cantidad_a = cadena1.lower().count(letra)

    if cadena2.lower().count(letra) > cantidad_a:
        con_mas_a = cadena2
    if cadena3.lower().count(letra) > cantidad_a:
        con_mas_a = cadena3
    if cadena4.lower().count(letra) > cantidad_a:
        con_mas_a = cadena4

    return print(con_mas_a)
      
   
cadena1 = str(input("ingrese cadena 1: "))
cadena2 = str(input("ingrese cadena 2: "))
cadena3 = str(input("ingrese cadena 3: "))
cadena4 = str(input("ingrese cadena 4: "))

cadena_mas(cadena1, cadena2, cadena3, cadena4 )
