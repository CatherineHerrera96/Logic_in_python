import calculadora_indices as calc4

def ejecutar_calcular_calorias_actividad (peso : float, altura : float, edad : int, valor_genero :float, valor_actividad : float) -> float:
    return calc4.calcular_calorias_en_actividad (peso, altura, edad,valor_genero, valor_actividad)

peso = float(input("ingrese el peso de la persona (en kilogramos):"))
altura = float(input("ingrese la altura de la persona (en centimetros): "))
edad = int(input("Ingrese la edad de la persona (en años): "))
valor_genero = float(input("Ingrese el valor 10.8 en caso de tener genero masculino o 0 en caso de ser mujer:" ))
valor_actividad = float(input("Ingrese el valor correspondiente según su grado de actividad: \n 1.2 para poco o ningún ejercicio \n 1.375 para ejercicio ligero \n 1.55 para ejercicio moderado \n 1.725 para deportistas \n 1.9 para atletas:  "))

Cactividad = ejecutar_calcular_calorias_actividad (peso,altura,edad,valor_genero, valor_actividad)
print (Cactividad)