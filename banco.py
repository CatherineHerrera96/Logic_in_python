numero_pesos = float(input("introduzca numero de numero de pesos: "))
tasa_interes = float(input("introduzca la tasa de intereses: "))
numero_a�os = int(input("introduzca numero de a�os: "))


C = numero_pesos
X = tasa_interes
n = numero_a�os

valor_futuro = C * (1 + (X/100))**n
print("el valor que se pagara en el futuro es de : " + str(round(valor_futuro)) + ", transcurridos " + str(n) + " a�os" + " " + "a una tasa anual del" + " " + str(X) + "%")
