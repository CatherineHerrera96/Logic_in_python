"""
Considere el software que se ejecuta en una máquina expendedora. Una de las tareas que debe realizar es determinar cuánto cambio debe entregarle al cliente luego de que paga.
Escriba una función que recibe la cantidad de dinero (en pesos) a dar como cambio al cliente y retorne un mensaje con la cantidad de monedas de 
cada denominación que deben ser entregadas, teniendo en cuenta que el cambio se debe otorgar con la menor cantidad de monedas posible.

La máquina cuenta con monedas de 500, 200, 100 y 50 pesos, y el cambio total se entregará con monedas de estas denominaciones. 
El mensaje retornado DEBE seguir el siguiente formato: “A,B,C,D” (sin espacios intermedios) donde A, B, C y D son la cantidad de monedas de 500, 200, 100 y 50, respectivamente


Consider software running on a vending machine. One of the tasks you need to perform is to determine how much change you should deliver to the customer after they pay.
Type a function that receives the amount of money (in pesos) to be given as a change to the client and return a message with the amount of coins of
each denomination that must be delivered, taking into account that the change must be granted with the least amount of coins possible.

The machine has coins of 500, 200, 100 and 50 pesos, and the total exchange will be delivered with coins of these denominations.
The returned message MUST follow the following format: "A,B,C,D" (without spaces in between) where A, B, C and D are the number of coins of 500, 200, 100 and 50, respectively.



@CatherineHerrera96
"""

def moneda500 (dinero : int) -> int:
    monedas500 = dinero // 500
    return monedas500

def moneda200 (dinero : int) -> int:
    monedas200 = (dinero % 500) // 200
    return monedas200

def moneda100 (dinero : int) -> int:
    monedas100 = ((dinero % 500) % 200) // 100
    return monedas100

def moneda50 (dinero : int) -> int:
    monedas50 = (((dinero % 500) % 200) % 100) // 50
    return monedas50

def cambio (dinero : int) -> str:
    return moneda500(dinero) , moneda200(dinero), moneda100(dinero) , moneda50(dinero)

dinero = int(input("ingrese la cantidad de cambio a regresar: "))


cambios = cambio(dinero)

print(cambios)