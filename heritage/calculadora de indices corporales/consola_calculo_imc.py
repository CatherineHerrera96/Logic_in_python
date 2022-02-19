import calculadora_indices as calc

def ejecutar_calcular_imc (peso : float, altura : float) -> float:
    return calc.calcular_IMC (peso, altura)

peso = float(input("ingrese el peso de la persona (en kilogramos):"))
altura = float(input("ingrese la altura de la persona (en metros): "))

IMC = ejecutar_calcular_imc(peso,altura)
print (IMC)
