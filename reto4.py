import json
suma = []
 

with open("D:/Users/JANUS/Documents/programacion/json/tienda 1.json", "r") as tienda1:
  t1 = json.load(tienda1)


with open("D:/Users/JANUS/Documents/programacion/json/faltantes.json", "r") as f1:
  cfaltantes = json.load(f1)



  for elemento in t1:
    for elemento2 in cfaltantes:
      if elemento == elemento2:
        print(elemento)
        print(t1[elemento])
         
  