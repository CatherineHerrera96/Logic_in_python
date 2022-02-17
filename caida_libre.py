"""
Crea una función que determine la velocidad, en (m/s), a la que viaja un objeto cuando toca el suelo, en caída libre. 
La función recibe la altura a la que se encontraba el objeto al soltarse, en metros.
Como es caída libre, la velocidad inicial del objeto es de 0 m/s . Asume que la aceleración debido a la gravedad es de 9.8 m/s^2. 
Puedes usar la siguiente fórmula para calcular la velocidad final (vf), donde v0 es la velocidad inicial, a es la aceleración y d la distancia al suelo. 

Creates a function that determines the speed, in (m/s), at which an object travels when it touches the ground, in free fall.
The function receives the height at which the object was when it was released, in meters.
As it is free fall, the initial velocity of the object is 0 m/s. It assumes that the acceleration due to gravity is 9.8 m/s^2.
You can use the following formula to calculate the final velocity (vf), where v0 is the initial velocity, a is the acceleration, and d is the ground clearance. 

@CatherineHerrera96
"""

import math

def vel_caida_libre (altura:float)->float:
    Velocidad = 0
    aceleracion = 9.8
    return math.sqrt(Velocidad + 2 * aceleracion * altura)

altura = float(input("ingrese la altura desde el suelo a la que es arrojada el objeto: "))

velocidad_final = vel_caida_libre(altura)

print (round(velocidad_final,2))

