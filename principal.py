import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import funcoes

#pontos_da_bola
pontos_em_x_da_posicao_bola = []
pontos_em_y_da_posicao_bola = []
#pontos_em_x_da_velocidade_bola = []
#pontos_em_y_da_velocidade_bola = []
#pontos_em_x_da_aceleracao_bola = []
#pontos_em_y_da_aceleracao_bola = []

#pontos do robô
pontos_em_x_da_posicao_robo = []
pontos_em_y_da_posicao_robo = []
#pontos_em_x_da_velocidade_robo = []
#pontos_em_y_da_velocidade_robo = []
#pontos_em_x_da_aceleracao_robo = []
#pontos_em_y_da_aceleracao_robo = []


#pedindo informações do robô
x_do_robo = float(input("Digite a posição do robô no eixo X: "))
y_do_robo = float(input("Digite a posição do robô no eixo Y: "))

#funcoes que armazena os dados dos pontos x e y da bola em minhas listas das posições.
funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_da_bola_em_x, pontos_em_x_da_posicao_bola)
funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_da_bola_em_y, pontos_em_y_da_posicao_bola)

#Cria o gráfico da trajetória da bola.
#funcoes.grafico_trajetoria_da_bola(pontos_em_x_da_posicao_bola, pontos_em_y_da_posicao_bola)

funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_robo_x,pontos_em_x_da_posicao_robo)
funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_robo_y, pontos_em_y_da_posicao_robo)

fig, ax = plt.subplots()  
ax.plot(pontos_em_x_da_posicao_robo, pontos_em_y_da_posicao_robo)
ax.plot(pontos_em_x_da_posicao_bola, pontos_em_y_da_posicao_robo)
ax.set_xlabel('X(m)')
ax.set_ylabel('Y(m)')
plt.show()








