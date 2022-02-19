import random #se importa la librería de python random

sujetos = ["QUERIDOS", "APRECIADOS", "DISTINGUIDOS", "HONORABLES", "ESTIMADOS", "RESPETADOS"]  #se define una lista
potenciales_marranos = ["COMPATRIOTAS", "CONCIUDADANOS", "AMIGOS", "COTERRANEOS", "COPARTIDARIOS", "ELECTORES"]
condicion = ["EN MI GOBIERNO", "CON SU APOYO", "SIENDO ELEGIDO", "CON SU AYUDA", "SI ME SIGUEN", "DURANTE MI MANDATO"]
compromiso = ["VOY A DERROTAR", "VENCERÉ", "ELIMINARÉ", "ACABARÉ", "LUCHARÉ CONTRA", "COMBATIRÉ"]
ilusion_guerrerista = ["LA VIOLENCIA Y", "LA DELINCUENCIA Y", "LA CORRUPCIÓN Y", "LA INFLACIÓN Y", "LA POBREZA Y", "EL DESPLAZAMIENTO Y"]
promesa = ["TRABAJARÉ POR", "GARANTIZARÉ", "PROTEGERÉ", "VELARÉ POR", "PROMOVERÉ", "DEFENDERÉ"]
beneficion_populista = ["LA EDUCACIÓN", "EL EMPLEO", "LA SEGURIDAD", "LA PAZ", "LA IGUALDAD", "LA SALUD"]
dependiendo_de_la_cantidad_votos = ["DEL PAÍS", "DE LA CIUDAD", "DE LA COMUNIDAD", "DE LA POBLACIÓN", "PARA TODA LA GENTE", "DE CADA COLOMBIANO"]

sujeto_seleccionado = random.choice(sujetos) #se utiliza la librería para seleccionar un elemento al azar de la lista sujetos
marrano_seleccionado = random.choice(potenciales_marranos)
condicion_seleccionado = random.choice(condicion)
compromiso_seleccionado = random.choice(compromiso)
ilusion_seleccionada = random.choice(ilusion_guerrerista)
promesa_seleccionada = random.choice(promesa)
beneficio_seleccionado = random.choice( beneficion_populista)
cantidad_seleccionada = random.choice (dependiendo_de_la_cantidad_votos)


print("Discurso generado: " + sujeto_seleccionado + " " + marrano_seleccionado + " " + condicion_seleccionado + " " + compromiso_seleccionado + " " + ilusion_seleccionada + " " + promesa_seleccionada + " " + beneficio_seleccionado + " " + cantidad_seleccionada)
