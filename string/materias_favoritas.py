"""
Pedro es un estudiante inteligente pero desinteresado por algunas de sus materias. A Pedro le gustan las clases en las que aprende programación, 
matemática, filosofía y literatura. Por lo anterior, cualquier materia que lleve en su título alguna de estas palabras, será de su agrado.
Pedro está planeando su horario, pero ha puesto a su asistente digital a que le dé posibles conjuntos de tres materias para inscribir en su semestre. 
Él quiere saber, dados los títulos de las tres materias, cuántas de estas son de su agrado. entradas sin tildes ni mayusculas.

Pedro is an intelligent but disinterested student in some of his subjects. Pedro likes classes where he learns programming,
mathematics, philosophy and literature. Therefore, any subject that has in its title any of these words, will be to your liking.
Pedro is planning his schedule, but has asked his digital assistant to give him possible sets of three subjects to enroll in his semester.
He wants to know, given the titles of the three subjects, how many of these are to his liking. entries without tildes or capital letters.

@CatherineHerrera96
"""
def conteo_de_materias (nombre_materia_1:str, nombre_materia_2:str, nombre_materia_3:str) -> int:
    contador = 0
    if "programacion" in nombre_materia_1 :
        contador += 1
    if "programacion" in nombre_materia_2:
        contador += 1
    if "programacion" in nombre_materia_3:
        contador +=1
    if "matematica" in nombre_materia_1:
        contador += 1
    if "matematica" in nombre_materia_2:
        contador +=1
    if "matematica" in nombre_materia_3:
        contador +=1
    if "filosofia" in nombre_materia_1:
        contador += 1
    if "filosofia" in nombre_materia_2:
        contador +=1
    if "filosofia" in nombre_materia_3:
        contador +=1
    if "literatura" in nombre_materia_1:
        contador += 1
    if "literatura" in nombre_materia_2:
        contador +=1
    if "literatura" in nombre_materia_3:
        contador +=1
    return contador

materia_1 = str(input("ingrese el nombre de la primera materia: "))
materia_2 = str(input("ingrese el nombre de la segunda materia: "))
materia_3 = str(input("ingrese el nombre de la tercera materia: "))

numero_materias_interes = conteo_de_materias(materia_1,materia_2, materia_3)

print (f"dentro de las materias ingresadas, {numero_materias_interes} pueden ser de interes para Pedro")
        
