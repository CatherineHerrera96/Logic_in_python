"""
programa que rota los valores de 3 variables enteras x1, x2, x3 hacias la derecha de forma que al final x2 tenga el valor inicial de x1, x3 el de x2 y x1 el de x3.
program that rotates the values of 3 integer variables x1, x2, x3 to the right so that at the end x2 has the initial value of x1, x3 that of x2 and x1 that of x3.
@CatherineHerrera96

"""


x1 = int (input("enter the first number:")) 
x2 = int (input("enter the second number:")) 
x3 = int (input("enter the third number:")) 

base = x1
x1 = x3
x3 = x2
x2 = base

print(x1)
print(x2)
print(x3) 