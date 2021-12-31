def calculo_ingresos (sueldo, prima, aguinaldo):
    ingresos_total = sueldo + (prima * 3 ) + aguinaldo
    return ingresos_total



salario = 500000
prima = 250000
bono_navidad = 200000
impuesto_renta = 100000

calculo_ingresos (salario, prima, bono_navidad)

resultado = calculo_ingresos(salario, prima, bono_navidad)

print (resultado)