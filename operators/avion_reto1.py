velocidad = int(input("ingrese el valor de la velocidad maxima del avion: "))

presion = int((2*(velocidad) + 4))
temperatura = int((velocidad + presion) / 5)

print(velocidad, "", presion, "", temperatura)



if temperatura < 20:
 print("uno")

if temperatura >= 20 and temperatura < 30:
 print("dos")

if temperatura >=30 and temperatura <= 50:
 print("tres")

if temperatura > 50: 
 print("cuatro")


