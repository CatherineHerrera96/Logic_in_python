lista = [3,2,1,1,1,3,2,1,1,1]
resultado=[]

for indice in lista:
  if indice not in resultado:
    resultado.append(indice)

print(resultado)




def laminas_faltantes_por_clase(indices, clases, clase_a_verificar):
  resultado = []
  # Algoritmo
  return resultado

laminas_faltantes_por_clase([1,3,6,8], [3,2,1,1,1,3,2,1,1,1], 1)



def laminas_faltantes(laminas_persona_1, laminas_persona_2):
  resultado = []
  # Algoritmo
  for indice in laminas_persona_1:
    if indice not in laminas_persona_2:
      resultado.append(indice)

  return resultado


result = laminas_faltantes([3,5,7,10,15,16], [4,10,5,8])
print (result)



def cantidad_laminas_cambiables(laminas_persona_1, laminas_persona_2):
  resultado = 0
  # Algoritmo
  for indice in laminas_persona_1:
    if indice in laminas_persona_2:
      resultado+=1
  return resultado


result2 = cantidad_laminas_cambiables([3,5,7,10,15,16], [4,10,5,8])
print (result2)


entrada1=[22, 28, 48, 54, 11, 88, 82, 100, 52, 14, 72, 69, 31, 89, 97, 81, 24, 74, 30, 32, 101, 102, 63, 104, 40, 80, 37, 45, 105, 57, 49, 90, 95, 62, 71, 64, 92, 13, 6, 83]

entrada2 = [93, 85, 87, 32, 66, 101, 53, 46, 25, 20, 43, 28, 79, 45, 78, 7, 26, 104, 44, 4, 88, 10, 21, 100, 72, 42, 58, 37, 70, 2, 92, 102, 38, 18, 0, 83, 95, 17, 89, 47, 40, 15, 23, 62, 14, 19, 56, 16, 63]


opt = [i for i in entrada1 if i not in entrada2] 
opt1 = [i for i in entrada2 if i not in entrada1]
