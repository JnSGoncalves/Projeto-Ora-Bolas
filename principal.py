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
interceptacoes_x = []
interceptacoes_y = []
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

#função do raio de interceptação
funcoes.raio_de_interceptação(pontos_em_x_da_posicao_robo, pontos_em_x_da_posicao_bola, 
pontos_em_y_da_posicao_robo,pontos_em_y_da_posicao_bola, interceptacoes_x, interceptacoes_y)




# Exibe o gráfico da trajetória da bola e do robô
fig, ax = plt.subplots()  
# Plotagem dos dados com diferentes cores
plt.plot(interceptacoes_x, interceptacoes_y,color='blue', label='Robô', )
plt.plot(pontos_em_x_da_posicao_bola, pontos_em_y_da_posicao_bola,color='yellow', label='Bola', )
plt.scatter(interceptacoes_x[-1],interceptacoes_y[-1], color='green', label='Ponto de Encontro', s=20)
# Adicionando legenda
plt.legend()
# Definindo a cor do texto da legenda
plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
plt.legend().get_texts()[1].set_color("yellow")  # Bola em amarelo
plt.legend().get_texts()[2].set_color("green")
plt.text(0.8, 4, f'x: {interceptacoes_x[-1]}, y: {interceptacoes_y[-1]}', fontsize=12, color='green')
ax.set_xlabel('X(m)')
ax.set_ylabel('Y(m)')
ax.set_title('Gráfico da Trajetória da Bola')
plt.show()
