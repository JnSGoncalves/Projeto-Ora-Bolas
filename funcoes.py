'''
Funções da bola com a variável tempo

função da posição 
--> X(t) = 0.005t³ -0.00000000000007t² +  0.5t+ 1
--> Y(t) = -0,02t² + 0,9t + 0,5

Função da velocidade
--> Vx(t) = 0,015t² -0,0003t + 0,5
--> Vy(t) = -0,04 + 0,9004

 Função da aceleração
 --> Ax(t) = 0,03t - 0,0006t
 --> Ay(t) = -0,04

'''



def posicao_da_bola_em_x(t=0):
    x = round(0.005 * t**3 -0.000000000000007* t**2 + 0.5*t + 1, 8)
    return x

def posicao_da_bola_em_y(t):
    y = -0.02 * t**2 + 0.9 * t + 0.5
    return y

def return_pontos_exatos_da_funcao(funcao, lista_desejada):
    tempo = 0
    for _ in range(6):
        resultado = funcao(tempo) 
        lista_desejada.append(resultado)
        tempo += 0.02


