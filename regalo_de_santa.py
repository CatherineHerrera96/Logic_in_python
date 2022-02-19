"""
En el taller de regalos de Santa Claus, el CTE (Chief Technology Elf) ha decidido implementar un nuevo sistema de clasificación de regalos, 
para facilitar su organización. Cada paquete tiene ahora un identificador numérico único. El identificador es un número entero entre 100 y 999, y
sirve para clasificar los regalos de la siguiente manera.
    Si el número es palíndromo e impar, el regalo corresponde a una niña.
    Si el número es palíndromo y par, el regalo corresponde a un niño.
    Si el número es par pero no es palíndromo, el regalo corresponde a un hombre.
    Si el número es impar pero no es palíndromo, el regalo corresponde a una mujer.
Escriba una función que ayude al CTE a calcular, dado un identificador único de regalo, a qué tipo de persona corresponde dicho regalo.

At the Santa Claus gift workshop, the CTE (Chief Technology Elf) has decided to implement a new gift sorting system,
to facilitate its organization. Each package now has a unique numeric identifier. The identifier is an integer between 100 and 999, and
it serves to classify gifts as follows.
    If the number is palindrome and odd, the gift corresponds to a girl.
    If the number is palindrome and even, the gift corresponds to a child.
    If the number is even but not palindrome, the gift corresponds to a man.
    If the number is odd but not palindrome, the gift corresponds to a woman.
Write a function that helps the CTE calculate, given a unique gift identifier, what type of person the gift corresponds to.

@CatherineHerrera96
"""
def es_palindromo (id: str)->bool:
    igual, aux = 0,0
    for ind in reversed(range(0, len(id))):
        if id[ind].lower() == id[aux].lower():
            igual += 1
        aux += 1 

    if len(id) == igual:
        return True
    else:
        return False

def es_par (id: str)->bool:
    x = int(id)
    if (x % 2 == 0):
        return True
    else:
        return False

def clasificar_regalo (palindromo : bool, par : bool) -> str:

    if (palindromo == True) and (par == True):
        print ("boy")
    if (palindromo == True) and (par == False):
        print ("girl")
    if (palindromo == False) and (par == True):
        print ("man")
    if (palindromo == False) and (par == False):
        print ("woman")
id = str(input("ingrese el numero del regalo (entre 100 y 999):"))


palindromo = es_palindromo(id)
par = es_par(id)

clasificacion = clasificar_regalo (palindromo, par)
    