"""
Nos piden crear un programa que permita calcular el valor del pasaje aéreo desde la ciudad de Bogotá hasta Tokio.
El valor dependerá de una tarifa básica, la compañia aérea elegida para el viaje, la temporada, la edad del pasajero y si es o no estudiante. 
Para calcular el precio, nos dicen que tenemos que tener en cuenta que la compañía ALAS incremente el valor de sus pasajes en un 30% en alta temporada, 
mientras que la compañía VOLAR lo incrementa solo en 20%. Ambas compañías descuentan el 50% si el pasajero es menor de edad. Además, 
la compañía VOLAR tiene un recargo de 100.000 pesos para los pasajeros mayores de 60 años para cubrir el seguro de vida.
Los estudiantes que viajan por ALAS y que no son menores de edad tienen un descuento de 10% en temporada baja. Y la tarifa básica Bogotá-Tokio reglamentaria
 es de 5.000.000 de pesos.

They ask us to create a program that allows us to calculate the value of the airfare from the city of Bogotá to Tokyo.
The value will depend on a basic fare, the airline chosen for the trip, the season, the age of the passenger and whether or not he is a student. 
To calculate the price, we are told that we have to take into account that the company ALAS increases the value of its tickets by 30% in high season,
while the company VOLAR increases it by only 20%. Both companies deduct 50% if the passenger is a minor. In addition
the company VOLAR has a surcharge of 100,000 pesos for passengers over 60 years of age to cover life insurance.
Students traveling through ALAS and who are not minors have a 10% discount in low season. And the basic rate Bogotá-Tokyo regulation
is 5,000,000 pesos.

@CatherineHerrera96
"""
#funcion que calcula el precio final deacuerdo a los parametroa a recibir


def Calcular_pasaje ( temporada_alta: bool, compañia : str, edad : int, estudiante: bool)-> int:
    precio = 5000000
    variaciones = 0
    seguro = False

    if compañia == "ALAS":
        if temporada_alta == True:
            variaciones += 0.3
        else:
            if edad >= 18 and estudiante:
                variaciones -= 0.1

    elif compañia == "VOLAR":
        if temporada_alta == True:
            variaciones -= 0.2
        if edad > 60:
            seguro = True

    if edad < 18:
        variaciones -= 0.5

    precio *= (1+ variaciones)
    
    if seguro == True:
        precio += 100000


    return round(precio)

#programa principal que recibe la informacion 

temporada = bool(int(input("¿es temporadad alta? ingrese 1 para SI y 0 para NO:")))
compañia = str(input("ingrese la compañia con la que quiere viajar (ALAS o VOLAR):"))
edad = int(input("ingrese la edad del pasajero:"))
estudiante = bool(int(input("¿es estudiante? ingrese 1 para Si y 0 para NO:")))

#en tarifa guardamos el pasaje calculado que se guardo al invocar la función
tarifa = Calcular_pasaje(temporada, compañia, edad, estudiante)

print (f"La tarifa del pasaje es de {tarifa} pesos colombianos")



