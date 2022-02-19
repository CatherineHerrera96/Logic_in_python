"""
defina funciones para convertir grados en las diferentes escalas 


@CatherineH
"""
def fahrenheit_a_centigrados (gradosF : float) -> float:   
    return  (gradosF - 32)*(5/9)

def centigrados_a_fahrenheit (gradosC : float) -> float:
    return (gradosC*(9/5))/1.8

gradosF = float(input("ingrese los grados fahrenheit que quiere convertir a centigrados: "))
gradosC = float(input("ingrese los grados centigrados que quiere convertir a fahrenheit: "))


CaF  = centigrados_a_fahrenheit(gradosC)
print(f"{gradosC} grados centigrados son iguales a {round(CaF,1)} grados fahrenheit")

FaC = fahrenheit_a_centigrados(gradosF)
print(f"{gradosF} grados fahrenheit son iguales a {round(FaC,1)} grados centigrados")
