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

#variável que pega o tempo em que o robô e a bola se encontram.
tempo_interceptacao = funcoes.tempo_robo(interceptacoes_x)



# Gráfico de interceptação entre o robô e a bola
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
plt.text(0.8, 4.5, f'Tempo: {tempo_interceptacao}', fontsize=12, color='green')
ax.set_xlabel('X(m)')
ax.set_ylabel('Y(m)')
ax.set_title('Gráfico da interceptação entre o robô e a bola')
plt.show()

while True:
    print("Digite o gráfico que deseja ver: ")
    print('''1 --> Gráfico da trajetória em X e Y entre o robô e a bola.
             2 --> Gráfico da posição em X do robô e a bola.
             3 --> Gráfico da posicão em Y do robô e a bola.
             4 --> Gráfico da Velocidade em X do robô e a bola.
             5 --> Gráfico da velocidade em Y do robô e a bola.
             6 --> Gráfico da aceleração em X do robo e a bola.
             7 --> Gráfico da aceleração em Y do robo e a bola.
             8 --> Gráfico da distância entre o robô e a bola.''')
    print()
    
