m1 = int(input("ingresa la masa en Kg de la masa n 1: "))
m2 = int(input("ingresa la masa en kg de la masa n 2: "))
r = int(input("ingrese en metros la distancia entre las masas: "))
G : float = 6.667384e-11

F = G * ((m1 * m2) / (r*r))

print(F)
