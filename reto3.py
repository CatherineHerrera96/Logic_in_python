Vuelos=input().split(" ")
listaVuelos=[Vuelos[0]]
listaFrecuencias=[]
count=1
for i in range(0,len(Vuelos)-1):
  if Vuelos[i]==Vuelos[i+1]: 
    count+=1 
  else:
    listaFrecuencias.append(str(count))
    count=1
    listaVuelos.append(Vuelos[i+1])
listaFrecuencias.append(str(count))
print(" ".join(listaVuelos))
print(" ".join(listaFrecuencias))


