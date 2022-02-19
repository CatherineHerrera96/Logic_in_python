"""
programa en el cual se ingresa una cantidad de pesos, una tasa de interes y un numero de años. 
El programa calcula en cuanto se abra convertido el capital inicial transcurridos el numero de años con el interes introducido.
recuerde que un capital de C pesos a un interes del x por cien durante n años se expres C*(1+x/100)^n pesos.

program in which a number of pesos, an interest rate and a number of years are entered.
The program calculates as soon as the initial capital is converted after the number of years with the interest entered.
remember that a capital of C pesos at an interest of x percent for n years is expressed C(1+x/100)^n pesos.

@CatherineHerrera96

"""

pesos = int(input("ingrese la cantidad de pesos a invertir:"))
anos = int(input("ingrese la cantidad de años que quiere invertir su dinero:"))
intereses = float(input("ingrese la tasa de intereses que va a manejar:"))

c = pesos
n = anos
x = intereses

ganancia = c*(1 + x/100)**n
print(f"El dinero que recibira transcurridos {anos} años es de {round(ganancia,2)} pesos con un interes del {intereses} %")
