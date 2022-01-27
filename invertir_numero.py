"""
programa que recibe un numero entero positivo de 4 cifras y devuelve el numero invertido.

program that receives a positive 4-digit integer and returns the inverted number.

@CatherineHerrera96
"""

def invertir_numero (numero : int) -> int :
    numero = numero [::-1]

    return (numero)


numero = input("ingrese el número de 4 digitos que desea invertir: ")
numero_invertido = invertir_numero(numero)

print(f"usted ingreso el número {numero} y su inverso respectivo es {numero_invertido}")


