"""
Cree una función que pueda calcular el índice de masa corporal (BMI) de una persona.
La fórmula para calcular el BMI es la siguiente: 
BMI = peso/(altura^2)
En esta fórmula el peso está en kilogramos y la altura en metros. Tenga en cuenta que el peso y altura que reciban su función, van a estar en libras y pulgadas respectivamente,
ya que su función será usada en los Estados Unidos.
Recuerde que:
1 libra corresponde a 0.45kg.
1 pulgada corresponde a 0.025 metros.

El valor de retorno debe estar redondeado a dos decimales. 

@CatherineH
"""

def calcula_BMI (peso : float, altura : float) -> float:
    peso = peso * 0.45
    altura = altura * 0.025
    BMI = ((peso)/(altura**2))
    return (round(BMI,2))


peso = float(input("ingrese su peso en libras:")) 
altura = float(input("ingrese su altura en pulgadas: "))  

calculo = calcula_BMI (peso,altura)
print(f"su indice de masa corporal (BMI) es {calculo}")