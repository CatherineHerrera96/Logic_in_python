"""
programa para determinar si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

program to determine if a year is leap. For a year to be leap year it must be divisible by 4 and it must not be divisible by 100, except that it is also divisible by 400.

@CatherineHerrera96
"""

year = int(input("ingrese el año que quiere determinar como bisiesto: ")) 


if year % 4 != 0: 
    print (f"el año {year} no es bisiesto")

elif year % 4 == 0 and year % 100 != 0:
    print (f"el año {year} es bisiesto")

elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: 
    print (f"el año {year} es bisiesto")

elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print (f"el año {year} no es bisiesto")
