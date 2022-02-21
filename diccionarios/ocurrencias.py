"""
 Nos solicitan contar la cantidad de ocurrencias o veces que aparece cada uno de los dígitos del cero al nueve dentro de un numero de diez cifras.

 We are asked to count the number of occurrences or times each of the digits from zero to nine appears within a ten-digit number.
@CatherineHerrera96
"""
#la funcion contador recib el numero ingresado, saca el modulo de este y lo almacena en la variable digito, en caso de exitir dentro del diccionario sumara uno a su respectiva llave, 
#de lo contrario creara un par de datos dentro del diccionario y retonara esre al programa principal

def contador (num : int, diccionario : dict) -> dict:
    digito = num % 10
    if digito in diccionario:
        diccionario[digito] += 1
    else:
        diccionario[digito] = 1
    return diccionario

#PROGRAMA PRINCIPAL 

numero = int(input("ingrese el numero de 10 cigras a analizar: "))
conteo = {}
#repeticion 1
conteo = contador (numero, conteo)

numero = numero // 10
#repeticion 2
conteo = contador (numero, conteo)

numero = numero // 10
#repeticion 3
conteo = contador (numero, conteo)

numero = numero // 10
#repeticion 4
conteo = contador (numero, conteo)

numero = numero // 10
#repeticion 5
conteo = contador (numero, conteo)

numero = numero // 10
#repeticion 6
conteo = contador (numero, conteo)

numero = numero // 10
#repeticion 7
conteo = contador (numero, conteo)

numero = numero // 10
#repeticion 8
conteo = contador (numero, conteo)

numero = numero // 10
#repeticion 9
conteo = contador (numero, conteo)

numero = numero // 10
#repeticion 10
conteo = contador (numero, conteo)

print (conteo)



