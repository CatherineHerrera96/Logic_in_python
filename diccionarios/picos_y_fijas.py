"""
@CatherineHerrera96
"""


def picas_y_fijas (numero_secreto: int, intent: int) -> dict:
    diccionario = {"PICAS" : 0, "FIJAS" : 0}
    adivinar = intent

    #primer numero
    a = numero_secreto % 10
    b = intent % 10
    if a == b:
        diccionario["FIJAS"] += 1
    elif str(a) in str(adivinar):
        diccionario["PICAS"] += 1
    #segundo numero 
    numero_secreto = numero_secreto // 10
    intent = intent // 10
    a = numero_secreto % 10
    b = intent % 10
    if a == b:
        diccionario["FIJAS"] += 1
    elif str(a) in str(adivinar):
        diccionario["PICAS"] += 1
    #tercer numero 
    numero_secreto = numero_secreto // 10
    intent = intent // 10
    a = numero_secreto % 10
    b = intent % 10
    if a == b:
        diccionario["FIJAS"] += 1
    elif str(a) in str(adivinar):
        diccionario["PICAS"] += 1
    #cuarto numero 
    numero_secreto = numero_secreto // 10
    intent = intent // 10
    a = numero_secreto % 10
    b = intent % 10
    if a == b:
        diccionario["FIJAS"] += 1
    elif str(a) in str(adivinar):
        diccionario["PICAS"] += 1

    
    return diccionario


#PROGRAMA PRINCIPAL

numero_secreto = int(input("ingrese el numero de 4 cifras: "))
intent = int(input("ingrese el numero que cree adivinar: "))


#primer numero
picos_fijas = picas_y_fijas(numero_secreto, intent)




print (picos_fijas)

