import calculadora_indices as calc2

def ejecutar_calcular_porcentaje_grasa (peso : float, altura : float, edad : int, valor_genero :float) -> float:
    return calc2.calcular_porcentaje_grasa (peso, altura, edad,valor_genero)

peso = float(input("ingrese el peso de la persona (en kilogramos):"))
altura = float(input("ingrese la altura de la persona (en metros): "))
edad = int(input("Ingrese la edad de la persona (en años): "))
valor_genero = float(input("Ingrese el valor 10.8 en caso de tener genero masculino o 0 en caso de ser mujer:" ))

PG = ejecutar_calcular_porcentaje_grasa(peso,altura,edad,valor_genero)
print (PG)