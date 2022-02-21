"""
Usted quiere anticipar el movimiento del nuevo robot que recibió como regalo de cumpleaños. El robot tiene una brújula interna que le permite saber hacia qué punto cardinal 
está mirando actualmente: Norte, Sur, Este, u Oeste. Además, el robot tiene un control remoto que permite girarlo hacia la izquierda o la derecha,
y también pedirle que dé media vuelta. Usted debe escribir una función que, dados 3 comandos que se envíen usando el control remoto, calcule la orientación final del robot.
La representación de los puntos cardinales que llegan por parámetro es la siguiente: "N", para Norte, "S", para Sur, "E", para Este y "W", para Oeste.
Las representaciones de los comandos del control remoto llegan asi; "L", para girar a la izquierda, "R", para girar a la derecha, "H", para dar media vuelta, y ".", para mantener la orientación actual.   

You want to anticipate the movement of the new robot you received as a birthday present. The robot has an internal compass that allows it to know to which cardinal point
is currently looking: North, South, East, or West. In addition, the robot has a remote control that allows it to be turned left or right,
and also ask him to turn around. You must write a function that, given 3 commands that are sent using the remote control, calculates the final orientation of the robot.
The representation of the cardinal points that arrive by parameter is as follows: "N", for North, "S", for South, "E", for East and "W", for West.
The representations of the remote control commands arrive like this; "L", to turn left, "R", to turn right, "H", to turn around, and ".", to maintain the current orientation. 
@CatherineHerrera96
"""

def movimiento_robot(orientacion_actual:str, giro_1:str, giro_2:str, giro_3:str)->str:
      
    if orientacion_actual == "N" and giro_1 == "L":
        orientacion_actual = "W"
    elif orientacion_actual == "N" and giro_1 == "R":
        orientacion_actual = "E"
    elif orientacion_actual == "N" and giro_1 == "H":
        orientacion_actual = "S"
    elif orientacion_actual == "N" and giro_1 == ".":
        orientacion_actual = "N"
    elif orientacion_actual == "E" and giro_1 == "R":
        orientacion_actual = "S"
    elif orientacion_actual == "E" and giro_1 == "L":
        orientacion_actual = "N"
    elif orientacion_actual == "E" and giro_1 == "H":
        orientacion_actual = "W"
    elif orientacion_actual == "E" and giro_1 == ".":
        orientacion_actual = "E"
    elif orientacion_actual == "W" and giro_1 == "R":
        orientacion_actual = "N"
    elif orientacion_actual == "W" and giro_1 == "L":
        orientacion_actual = "S"
    elif orientacion_actual == "W" and giro_1 == "H":
        orientacion_actual = "E"
    elif orientacion_actual == "W" and giro_1 == ".":
        orientacion_actual = "W"
    elif orientacion_actual == "S" and giro_1 == "R":
        orientacion_actual = "W"
    elif orientacion_actual == "S" and giro_1 == "L":
        orientacion_actual = "E"
    elif orientacion_actual == "S" and giro_1 == "H":
        orientacion_actual = "N"
    elif orientacion_actual == "S" and giro_1 == ".":
        orientacion_actual = "S"
    
    orientacion_actual = orientacion_actual
    
    if orientacion_actual == "N" and giro_2 == "L":
        orientacion_actual = "W"
    elif orientacion_actual == "N" and giro_2 == "R":
        orientacion_actual = "E"
    elif orientacion_actual == "N" and giro_2 == "H":
        orientacion_actual = "S"
    elif orientacion_actual == "N" and giro_2 == ".":
        orientacion_actual = "N"
    elif orientacion_actual == "E" and giro_2 == "R":
        orientacion_actual = "S"
    elif orientacion_actual == "E" and giro_2== "L":
        orientacion_actual = "N"
    elif orientacion_actual == "E" and giro_2 == "H":
        orientacion_actual = "W"
    elif orientacion_actual == "E" and giro_2 == ".":
        orientacion_actual = "E"
    elif orientacion_actual == "W" and giro_2 == "R":
        orientacion_actual = "N"
    elif orientacion_actual == "W" and giro_2 == "L":
        orientacion_actual = "S"
    elif orientacion_actual == "W" and giro_2 == "H":
        orientacion_actual = "E"
    elif orientacion_actual == "W" and giro_2 == ".":
        orientacion_actual = "W"
    elif orientacion_actual == "S" and giro_2 == "R":
        orientacion_actual = "W"
    elif orientacion_actual == "S" and giro_2 == "L":
        orientacion_actual = "E"
    elif orientacion_actual == "S" and giro_2 == "H":
        orientacion_actual = "N"
    elif orientacion_actual == "S" and giro_2 == ".":
        orientacion_actual = "S"
    
    orientacion_actual  = orientacion_actual
    
    if orientacion_actual == "N" and giro_3 == "L":
        orientacion_actual = "W"
    elif orientacion_actual == "N" and giro_3 == "R":
        orientacion_actual = "E"
    elif orientacion_actual == "N" and giro_3 == "H":
        orientacion_actual = "S"
    elif orientacion_actual == "N" and giro_3 == ".":
        orientacion_actual = "N"
    elif orientacion_actual == "E" and giro_3 == "R":
        orientacion_actual = "S"
    elif orientacion_actual == "E" and giro_3 == "L":
        orientacion_actual = "N"
    elif orientacion_actual == "E" and giro_3 == "H":
        orientacion_actual = "W"
    elif orientacion_actual == "E" and giro_3 == ".":
        orientacion_actual = "E"
    elif orientacion_actual == "W" and giro_3 == "R":
        orientacion_actual = "N"
    elif orientacion_actual == "W" and giro_3 == "L":
        orientacion_actual = "S"
    elif orientacion_actual == "W" and giro_3 == "H":
        orientacion_actual = "E"
    elif orientacion_actual == "W" and giro_3 == ".":
        orientacion_actual = "W"
    elif orientacion_actual == "S" and giro_3 == "R":
        orientacion_actual = "W"
    elif orientacion_actual == "S" and giro_3 == "L":
        orientacion_actual = "E"
    elif orientacion_actual == "S" and giro_3 == "H":
        orientacion_actual = "N"
    elif orientacion_actual == "S" and giro_3 == ".":
        orientacion_actual = "S"
    
    return orientacion_actual

orientacion_actual = str(input("ingrese orientación actual (N,S,E,O):"))
giro_1 = str(input("ingrese el primer giro del robot (L,R,H,.):"))
giro_2 = str(input("ingrese el segundo giro del robot (L,R,H,.):"))
giro_3 = str(input("ingrese el tercer giro del robot (L,R,H,.):"))  

movimiento = movimiento_robot (orientacion_actual,giro_1,giro_2,giro_3)
print (movimiento)






