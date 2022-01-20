"""
El área de un triángulo puede ser calculada cuando se conoce la longitud de sus lados. Teniendo en cuenta que s1, s2 y s3 son las longitudes de los lados del triángulo, 
se puede calcular el subperímetro s = (s1+s2+s3)/2, y, con este valor, se puede calcular el área del triángulo de la siguiente manera: area = √( s * (s-s1) * (s-s2) * (s-s3) ). 
Cree una función que recibe la medida de los lados del triángulo y retorna el área de este, redondeada a una cifra decimal.

The area of a triangle can be calculated when the length of its sides is known. Considering that s1, s2 and s3 are the lengths of the sides of the triangle,
you can calculate the subperimeter s = (s1+s2+s3)/2, and, with this value, you can calculate the area of the triangle as follows: area = √( s * (s-s1) * (s-s2) * (s-s3) ). 
Create a function that receives the measurement from the sides of the triangle and returns the area of the triangle, rounded to a decimal place.

@CatherineHerrera96
"""


import math

#
def area_triangulo (s1: int, s2 : int, s3 : int) -> int:
    s = (s1 + s2 + s3)/2
    area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    return area

s1 = int(input("ingrese el primer lado del triangilo: "))    
s2 = int(input("ingrese el segundo lado del triangilo: "))  
s3 = int(input("ingrese el tercer lado del triangilo: ")) 

solucion = area_triangulo(s1,s2,s3)
print(f"El area del traingulo es {round(solucion,1)}")