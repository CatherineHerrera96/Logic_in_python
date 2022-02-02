"""
Una agencia de viajes necesita informar a sus clientes la hora de llegada de sus vuelos. Se conoce la hora de partida del vuelo (en horas, minutos y segundos) y la duración del vuelo (en horas, minutos y segundos).
Cree una función que retorne la hora de llegada del vuelo en una cadena con el formato “HH:mm:ss” donde HH es la hora, mm los minutos y ss los segundos de la hora de llegada del vuelo. 
La hora está dada en formato de 24 horas. Si alguno de los 3 números de la respuesta es menor a 10, sólo se necesita un dígito ('7' en lugar de '07').

@CatherineHerrera96
"""

def Calcular_hora_llegada (hora_salida: int, duracion_horas: int ) -> int:
    llegada_hora = hora_salida - duracion_horas
    return llegada_hora

def Calcular_minuto_llegada (minuto_salida: int, duracion_minutos: int ) -> str:
    llegada_minuto = minuto_salida - duracion_minutos
    return llegada_minuto

def Calcular_segundo_llegada (segundo_salida: int, duracion_segundos: int ) -> str:
    llegada_segundo = segundo_salida - duracion_segundos
    return llegada_segundo

def calcular_tiempo_llegada (hora_salida: int, duracion_horas: int, minuto_salida: int, duracion_minutos: int, segundo_salida: int, duracion_segundos: int ) -> int :
    return Calcular_hora_llegada (hora_salida, duracion_horas), Calcular_minuto_llegada (minuto_salida, duracion_minutos) , Calcular_segundo_llegada (segundo_salida, duracion_segundos)


hora_salida = int(input("ingrese la hora de salida del vuelo(de 00 a 23):"))
minuto_salida = int(input("ingrese el minuto de salida del vuelo(de 00 a 59):"))
segundo_salida = int(input("ingrese el segundo de salida del vuelo(de 00 a 59):"))
duracion_horas = int(input("ingrese número de horas que dura el vuelo(): ")) 
duracion_minutos = int(input("ingrese número de minutos (adicionales al numero de horas) que dura el vuelo(): ")) 
duracion_segundos = int(input("ingrese número de segundos (adicionales al numero de horas y minutos) que dura el vuelo(): ")) 

#tiempo_llegada = calcular_tiempo_llegada(hora_salida, duracion_horas, minuto_salida, duracion_minutos, segundo_salida, duracion_segundos)
hora = Calcular_hora_llegada (hora_salida, duracion_horas)
minuto = Calcular_minuto_llegada (minuto_salida, duracion_minutos)
segundo = Calcular_segundo_llegada (segundo_salida, duracion_segundos)

print (f"la hora de llegada del vuelo es aproximadamente a las “{hora}:{minuto}:{segundo}” ")
