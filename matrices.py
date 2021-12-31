cantidad_de_filas = int(input("introducir cantidad de filas: "))
cantidad_de_columnas = int(input("introducir cantidad de columnas: "))

matrix = [ ]

for indice_fila in range(cantidad_de_filas):
  fila = [ ]
  for indice_columna in range(cantidad_de_columnas):
     componente = int(input(f"ingese el valor del componente en la f{indice_fila} y c{indice_columna}: "))
    
     fila.append(componente)

  matrix.append(fila) 

for fila in matrix:
  print(fila)