'''
Funções da bola com a variável tempo

função da posição 
--> X(t) = 0.005t³ -0.00000000000007t² +  0.5t+ 1
--> Y(t) = -0,02t² + 0,9t + 0,5

Função da velocidade
--> Vx(t) = 0,015t² -0,0003t + 0,5
--> Vy(t) = -0,04.t + 0,9004

 Função da aceleração
 --> Ax(t) = 0,03t - 0,0006t
 --> Ay(t) = -0,04

'''



import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from math import sqrt;


x_do_robo = float(input("Digite a posição do robô no eixo X: "))
y_do_robo = float(input("Digite a posição do robô no eixo Y: "))


#Funções da bola
def posicao_da_bola_em_x(t=0):
    x = round(0.005 * t**3 -0.000000000000007* t**2 + 0.5*t + 1, 8)
    return x

def posicao_da_bola_em_y(t=0):
    y = round(-0.02 * t**2 + 0.9 * t + 0.5, 6)
    return y

def velocidade_bola_x(t=0):
    vx = round((0.015*t**2) - 0.0003*t + 0.5 , 6)
    return vx

def velocidade_bola_y(t=0):
    vy = round(-0.04*t + 0.9004 , 6) 
    return vy


#Funções do robô
def posicao_robo_x(t=0):
    x = round(x_do_robo + 2.8*t + (2.8 * t**2/2), 8)
    return x

def posicao_robo_y(t=0):
    y = round(y_do_robo + 2.8*t + (2.8 * t**2/2), 6)
    return y

def Velocidade_robo_x(t=0):
    vx = round(2.8 + (2.8 * t) , 6)
    return vx

def velocidade_robo_y(t = 0):
    vy = round(2.8 + (2.8 * t) , 6)
    return vy



#função para armazenar todos os pontos desejados em uma lista.
def return_pontos_exatos_da_funcao(funcao, lista_desejada):
    tempo = 0
    for _ in range(343):
        resultado = funcao(tempo) 
        lista_desejada.append(resultado)
        tempo += 0.02

#Função que retorna o tempo inteiro do trajeto
def return_tempo(lista):
    tempo = 0
    for _ in range(343):
        if tempo in lista:
            pass
        else:
            lista.append(tempo)
            tempo += 0.02

#Exibe o gráfico da bola.
def grafico_trajetoria_da_bola(lista_x, lista_y):
    fig, ax = plt.subplots()  
    ax.plot(lista_x, lista_y, color='yellow', linestyle='-', linewidth=2) 
    ax.set_xlabel('X(m)')
    ax.set_ylabel('Y(m)')
    ax.set_title('Gráfico da Trajetória da Bola')
    ax.set_xlim(0, 52)  
    ax.set_ylim(0, 11) 
    ax.set_facecolor('green')
    plt.show()




#função que armazena os pontos de interceptações.
def raio_de_interceptação(x_robo, x_bola, y_robo, y_bola, lista_x, lista_y):
    for i in range(len(x_robo)):
        for j in range(len(x_bola)):
            distancia = sqrt((x_robo[i] - x_bola[j])**2 + (y_robo[i] - y_bola[j])**2)
            if distancia <= 0.1115:
                return True
            else:
                if x_robo[i] in lista_x or y_robo[i] in lista_y:
                    pass
                else:
                    lista_x.append(x_robo[i])
                    lista_y.append(y_robo[i])

#função que lê o tempo de encontro entre o robo e a bola
def tempo_robo(interceptacoes_x):
    # O tempo é igual ao número de pontos de interceptação multiplicado pelo intervalo de tempo (0.02)
    tempo = len(interceptacoes_x) * 0.02
    return round(tempo, 2)
    