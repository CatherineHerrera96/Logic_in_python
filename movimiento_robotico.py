"""

 N = 90 or -270
    S = 270 or -90
    O = 180 or -180
    E = 0 or 360
    L = + 90
    r = - 90
    h = + 180
    p = + 0 
    if orientacion_actual is N:
@CatherineHerrera96
"""

def movimiento_robot (orientacion_actual : str, giro_1 : str, giro_2 : str, giro_3 : str)-> str:
    N, S, O, E, L, R, H, P = 0, 0, 0, 0, 0, 0, 0, 0
    
    if orientacion_actual == N :
        N = 90
        if giro_1 == L :
            N += 90
        elif giro_1 == R:
            N -= 90
        elif giro_1 == H :
            N += 180
        elif giro_1 == P :
            N += 0

    elif orientacion_actual == S :
        S = 270
        if giro_1 == L :
            N += 90
        elif giro_1 == R:
            N -= 90
        elif giro_1 == H :
            N += 180
        elif giro_1 == P :
            N += 0
    elif orientacion_actual == E :
        E = 0
        
    elif orientacion_actual == O :
        O = 180
    L = + 90
    R = - 90
    H = + 180
    P = + 0 
  
    return  orientacion_actual + giro_1 + giro_2 + giro_3




orientacion_actual = str(input("ingrese orientación actual (N,S,E,O):"))
giro_1 = str(input("ingrese el primer giro del robot (L,R,H,.):"))
giro_2 = str(input("ingrese el segundo giro del robot (L,R,H,.):"))
giro_3 = str(input("ingrese el tercer giro del robot (L,R,H,.):"))  

movimiento = movimiento_robot (orientacion_actual,giro_1,giro_2,giro_3)
print (movimiento)






