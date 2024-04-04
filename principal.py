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




#funcão que armazena os pontos da bola em x e y.
funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_da_bola_em_x, pontos_em_x_da_posicao_bola)
funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_da_bola_em_y, pontos_em_y_da_posicao_bola)

#função que armazena os pontos do robo em x e y.
funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_robo_x,pontos_em_x_da_posicao_robo)
funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_robo_y, pontos_em_y_da_posicao_robo)


#pontos de encontro da posição do robô e da bola.
conjunto_x_bola = set(pontos_em_x_da_posicao_bola)
conjunto_x_robo = set(pontos_em_x_da_posicao_robo)
conjunto_y_bola = set(pontos_em_y_da_posicao_bola)
conjunto_y_robo = set(pontos_em_y_da_posicao_robo)
interceccao_conjuntos_x_posicao = conjunto_x_robo & conjunto_x_bola
interseccao_conjuntos_y_posicao = conjunto_y_bola & conjunto_y_robo




# Exibe o gráfico da trajetória da bola e do robô
fig, ax = plt.subplots()  
ax.plot(pontos_em_x_da_posicao_bola, pontos_em_y_da_posicao_bola, color='yellow', linestyle='-', linewidth=2) 
ax.plot(pontos_em_x_da_posicao_robo, pontos_em_y_da_posicao_robo, color="blue",linestyle='-', linewidth=2)
ax.set_xlabel('X(m)')
ax.set_ylabel('Y(m)')
ax.set_title('Gráfico da Trajetória da Bola')
plt.show()
