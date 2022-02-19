import calculadora_indices as calc3


def ejecutar_calcular_calorias_reposo (peso : float, altura : float, edad : int, valor_genero :float) -> float:
    return calc3.calcular_calorias_en_reposo (peso, altura, edad,valor_genero)

peso = float(input("ingrese el peso de la persona (en kilogramos):"))
altura = float(input("ingrese la altura de la persona (en centimetros): "))
edad = int(input("Ingrese la edad de la persona (en años): "))
valor_genero = float(input("Ingrese el valor 10.8 en caso de tener genero masculino o 0 en caso de ser mujer:" ))

Creposo = ejecutar_calcular_calorias_reposo (peso,altura,edad,valor_genero)
print (Creposo)