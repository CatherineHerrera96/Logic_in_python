        
    #se imprime la fila, esta funcion es llamada por la de ingresar matrix para mostrar a fila que guardo por medio de componentes
def mostrar_matrix (matrix_to_show):
   print("--------------")
   for fila in matrix_to_show:
    print(fila)

    #se añade el numero de filas y columnas... después pide añadir los comonentes que se ingresan en la fila y columna correspondiente 
def ingresar_matrix(): 

  cantidad_de_filas = int(input("introducir cantidad de filas: "))
  cantidad_de_columnas = int(input("introducir cantidad de columnas: "))

  new_matrix = [ ]

   #indice fila esta en el rango que determina la cantidad  de filas puesto arriba
   #indice columna bis y ambos van desde 0 a ---
   #componente: es el numero guardado en infice fila-indice columna 
  for indice_fila in range(cantidad_de_filas):
     fila = [ ]

     for indice_columna in range(cantidad_de_columnas):
         componente = int(input(f"ingese el valor del componente en la f{indice_fila} y c{indice_columna}: "))
         fila.append(componente)

     new_matrix.append(fila)

  mostrar_matrix(new_matrix) 

  return new_matrix    
#matrix1 seria la cantidad de columnas de la primera fila de la matrizx1
# aca bamos a ver si las matrices se pueden sumar, las condiciones es que tengan la misma cantidad de elemento
def se_pueden_sumar_las_matrices():
    if (len(matrix1) == 0) or (len(matrix2) == 0 ) or (len(matrix1) != len(matrix2)):
        return False


    for indice_fila in range(len(matrix1)):
        fila_a_verificar_matrix1 = matrix1[indice_fila]
        fila_a_verificar_matrix2 = matrix2[indice_fila]

        if not (cantidad_columnas == len(fila_a_verificar_matrix1)) and (cantidad_columnas == len(fila_a_verificar_matrix2)):
            return False

        
    return True


matrixA = ingresar_matrix()
matrixB = ingresar_matrix()

if not se_pueden_sumar_las_matrices(matrixA, matrixB):
    print("las matrices no se pueden sumar porque no tienen el mismo tamaño ")
    quit()