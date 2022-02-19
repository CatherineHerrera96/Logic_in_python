X1 = int(input("ingrese el valor de X1: " ))
X2 = int(input("ingrese el valor de X2: "))
X3 = int(input("ingrese el valor de X3: "))

guardar = X1
X1 = X3
X3 = X2
X2 = guardar



print(str(X1) + " , " + str(X2) + " , " + str(X3))