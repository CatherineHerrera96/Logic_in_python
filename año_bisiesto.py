ano = 1996  #año que queremos determinar como bisiesto o no 


if ano % 4 != 0: 
    print ("no es bisiesto")

elif ano % 4 == 0 and ano % 100 != 0:
    print ("es bisiesto")

elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0: 
    print("es bisiesto")

elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 != 0:
    print("no es bisiesto")
