"""
Crea una función que calcule la edad de una persona a partir de su fecha de nacimiento y la fecha actual.
Ambas fechas se proporcionan en años, meses y días, y la edad debe retornarse de la misma manera, en una cadena con la forma “aa,MM,dd”. 
Suponga que todos los meses son de 30 días. 

@CatherineHerrera96
"""

def calcular_edad (dia_nacio:int, mes_nacio:int,anio_nacio:int,dia_actual:int,mes_actual:int,anio_actual:int)->int:
    return (anio_actual - anio_nacio - 1), (mes_actual + 11  - mes_nacio), (dia_actual + 30 - dia_nacio)

dia_nacio = int(25)
mes_nacio = int(10)
anio_nacio = int(1993)
dia_actual = int(4)
mes_actual = int(8)
anio_actual = int(2019)

edad_actual = calcular_edad(dia_nacio, mes_nacio, anio_nacio, dia_actual,mes_actual,anio_actual)

print (edad_actual)
