

def calcular_IMC (peso : float, altura : float) -> float:
    IMC = ((peso)/(altura**2))
    return round(IMC,2)

def calcular_porcentaje_grasa (peso : float, altura : float, edad : int, valor_genero : float) -> float:
    GC = 1.2 * (peso / (altura * altura)) + 0.23 * edad - 5.4 - valor_genero
    return f"{round(GC,2)}%"

def calcular_calorias_en_reposo (peso : float, altura : float, edad : int, valor_genero : float) -> float:
    TMB = (10 * peso) + (6.25 * altura) - (5*edad) + valor_genero
    return f"{round(TMB,2)} cal"

def calcular_calorias_en_actividad (peso : float, altura : float, edad : int, valor_genero : float, valor_actividad : float) -> float:
    TMBF = ((10 * peso) + (6.25 * altura) - (5*edad) + valor_genero) * valor_actividad
    return f"{round(TMBF,2)} cal"

def consumo_calorias_recomendado_para_adelgazar (peso : float, altura : float, edad : int, valor_genero : float) -> float:
    TMB = (10 * peso) + (6.25 * altura) - (5*edad) + valor_genero
    xxx = TMB * 0.80
    yyy = TMB * 0.85
    return (f"Para adelgazar es recomendado que consumas entre: {round(xxx,2)} y {round(yyy,2)} calorías al día")

