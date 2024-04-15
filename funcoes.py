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


#Funções do robô
def posicao_robo_x(t=0):
    x = round(x_do_robo + 0.09*t + (0.09 * t**2/2),8)
    return x

def posicao_robo_y(t=0):
    y = round(y_do_robo + 0.09*t + (0.09 * t**2/2), 6)
    return y



#função para armazenar todos os pontos desejados em uma lista.
def return_pontos_exatos_da_funcao(funcao, lista_desejada):
    tempo = 0
    for _ in range(343):
        resultado = funcao(tempo) 
        lista_desejada.append(resultado)
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




#funções abaixo em teste ainda...
def calculo_raio_de_interceptação_return_x(x_robo, x_bola, y_robo, y_bola):
    indice = 0
    distancia = sqrt((x_robo[indice] - x_bola[indice])**2 + (y_robo[indice] - y_bola[indice])**2)

    pontos_interceptacao_x = [x_robo[0]]
    pontos_interceptacao_y = [y_robo[0]]

    while distancia > 0.1115:
        indice += 1
        distancia = sqrt((x_robo[indice] - x_bola[indice])**2 + (y_robo[indice] - y_bola[indice])**2)
        pontos_interceptacao_x.append(x_robo[indice])
        pontos_interceptacao_y.append(y_robo[indice])

    return pontos_interceptacao_x

def calculo_raio_de_interceptação_return_y(x_robo, x_bola, y_robo, y_bola):
    indice = 0
    distancia = sqrt((x_robo[indice] - x_bola[indice])**2 + (y_robo[indice] - y_bola[indice])**2)

    pontos_interceptacao_x = [x_robo[0]]
    pontos_interceptacao_y = [y_robo[0]]

    while distancia > 0.1115:
        indice += 1
        distancia = sqrt((x_robo[indice] - x_bola[indice])**2 + (y_robo[indice] - y_bola[indice])**2)
        pontos_interceptacao_x.append(x_robo[indice])
        pontos_interceptacao_y.append(y_robo[indice])

    return pontos_interceptacao_y