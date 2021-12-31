tiene_licencia_conduccion = bool(int(input("lincencia? si = 1 no = 0 ")))
cantidad_multas_transito = int(input("cantidad de multas de transito:  "))
cantidad_grados_de_alcohol_en_sangre = float(input("grado de alcohol en decimal:  "))
velocidad_vehiculo = float(input("velocidad del vehiculo en decimal:  "))
papeles_en_regla = bool(int(input("papeles en regla? si = 1  no = 0  ")))
vidrios_polarizados = bool(int(input("vidrios polarizados? si = 1  no = 0  ")))
edad_conductor = int(input("edad del conductor:  "))


el_vehiculo_puede_continuar = (tiene_licencia_conduccion == 1 ) and ( cantidad_multas_transito == 0) and (cantidad_grados_de_alcohol_en_sangre == 0) and (0 < velocidad_vehiculo <= 80) and ( papeles_en_regla == 1) and ( vidrios_polarizados == 0) and (18 <= edad_conductor <= 75)

print (el_vehiculo_puede_continuar)