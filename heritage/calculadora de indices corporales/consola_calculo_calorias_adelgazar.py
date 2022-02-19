import calculadora_indices as calc5

def ejecutar_calculo_calorias_adelgazar (peso: float, altura: float, edad: int, valor_genero: float) -> None:
    return calc5.consumo_calorias_recomendado_para_adelgazar (peso, altura, edad, valor_genero)
    
peso = float(input("ingrese el peso de la persona (en kilogramos):"))
altura = float(input("ingrese la altura de la persona (en centimetros): "))
edad = int(input("Ingrese la edad de la persona (en años): "))
valor_genero = float(input("Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer:" ))


Cadelgazar = ejecutar_calculo_calorias_adelgazar (peso, altura, edad, valor_genero)
print (Cadelgazar)


