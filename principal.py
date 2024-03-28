import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import funcoes

pontos_em_x_da_posicao = []
pontos_em_y_da_posicao = []
#pontos_em_x_da_velocidade = []
#pontos_em_y_da_velocidade = []
#pontos_em_x_da_aceleracao = []
#pontos_em_y_da_aceleracao = []

#pedindo informações do robô
x_do_robo = float(input("Digite a posição do robô no eixo X: "))
y_do_robo = float(input("Digite a posição do robô no eixo Y: "))

#funcoes que armazena os dados dos pontos x e y da bola em minhas listas das posições.
funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_da_bola_em_x, pontos_em_x_da_posicao)
funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_da_bola_em_y, pontos_em_y_da_posicao)

#Criando o gráfico da trajetória da bola.
fig, ax = plt.subplots()  
ax.plot(pontos_em_x_da_posicao, pontos_em_y_da_posicao)  
plt.show()







