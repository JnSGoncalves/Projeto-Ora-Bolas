import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import funcoes

lista_tempo = []

#pontos_da_bola
pontos_em_x_da_posicao_bola = []
pontos_em_y_da_posicao_bola = []
pontos_em_x_da_velocidade_bola = []
pontos_em_y_da_velocidade_bola = []
#pontos_em_x_da_aceleracao_bola = []
#pontos_em_y_da_aceleracao_bola = []

#pontos do robô
pontos_em_x_da_posicao_robo = []
pontos_em_y_da_posicao_robo = []
interceptacoes_x = []
interceptacoes_y = []
pontos_em_x_da_velocidade_robo = []
pontos_em_y_da_velocidade_robo = []
#pontos_em_x_da_aceleracao_robo = []
#pontos_em_y_da_aceleracao_robo = []


# GRÁFICO DE INTERCEPTAÇÃO DO ROBÔ EM X E Y.

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

#Adicionando os intervalos de tempo a lista_tempo
funcoes.return_tempo(lista_tempo)



#GRÁFICO PARA VELOCIDADE DO ROBÔ EM X E Y
funcoes.return_pontos_exatos_da_funcao(funcoes.velocidade_bola_x, pontos_em_x_da_velocidade_bola)
funcoes.return_pontos_exatos_da_funcao(funcoes.velocidade_bola_y, pontos_em_y_da_velocidade_bola)
print(pontos_em_x_da_velocidade_bola[0:10])
print(pontos_em_y_da_velocidade_bola[0:10])
input()




while True:
    print("Digite o gráfico que deseja ver: ")
    print('''
          1 --> Gráfico da trajetória em X e Y entre o robô e a bola.
          2 --> Gráfico da posição em X do robô e a bola.
          3 --> Gráfico da posicão em Y do robô e a bola.
          4 --> Gráfico da Velocidade em X do robô e a bola.
          5 --> Gráfico da velocidade em Y do robô e a bola.
          6 --> Gráfico da aceleração em X do robo e a bola.
          7 --> Gráfico da aceleração em Y do robo e a bola.
          8 --> Gráfico da distância entre o robô e a bola.
          0 --> Sair.''')
    opcao = int(input("Opção: "))

    print()
    if opcao == 1:
        # Gráfico de interceptação entre o robô e a bola
        fig, ax = plt.subplots()  
        # Plotagem dos dados com diferentes cores
        plt.plot(interceptacoes_x, interceptacoes_y,color='blue', label='Robô', )
        plt.plot(pontos_em_x_da_posicao_bola, pontos_em_y_da_posicao_bola,
                 color='yellow', label='Bola', )
        plt.scatter(interceptacoes_x[-1],interceptacoes_y[-1], 
                    color='green', label='Ponto de Encontro', s=20)
        # Adicionando legenda
        plt.legend()
        # Definindo a cor do texto da legenda
        plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
        plt.legend().get_texts()[1].set_color("yellow")  # Bola em amarelo
        plt.legend().get_texts()[2].set_color("green")
        plt.text(0.001, 4.2, f'Tempo: {tempo_interceptacao} s', fontsize=12, color='black')
        ax.set_xlabel('X(m)')
        ax.set_ylabel('Y(m)')
        ax.set_title('Gráfico da interceptação entre o robô e a bola')
        plt.show()

    elif opcao == 2:
        # Gráfico da trajetória do robô e da bola em função do tempo
        fig, ax = plt.subplots()  
        # Plotagem dos dados com diferentes cores
        plt.plot(lista_tempo[0:len(interceptacoes_x)], 
                 pontos_em_x_da_posicao_robo[0:len(interceptacoes_x)], 
                color='blue', label='Robô')
        plt.plot(lista_tempo[0:len(interceptacoes_x)],
                  pontos_em_x_da_posicao_bola[0:len(interceptacoes_x)], 
                color='yellow', label='Bola')
        # Adicionando legenda
        plt.legend()
        # Definindo a cor do texto da legenda
        plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
        plt.legend().get_texts()[1].set_color("yellow")  # Bola em amarelo
        # Adicionando texto com o tempo de interceptação
        ax.set_xlabel('Tempo (s)')
        ax.set_ylabel('Posição X (m)')
        ax.set_title('Trajetória do Robô e da Bola no eixo X em Função do Tempo')
        plt.show()

    elif opcao == 3:
        # Gráfico da trajetória do robô e da bola em função do tempo
        fig, ax = plt.subplots()  
        # Plotagem dos dados com diferentes cores
        plt.plot(lista_tempo[0:len(interceptacoes_y)], 
                 pontos_em_y_da_posicao_robo[0:len(interceptacoes_y)], 
                color='blue', label='Robô')
        plt.plot(lista_tempo[0:len(interceptacoes_y)], 
                 pontos_em_y_da_posicao_bola[0:len(interceptacoes_y)], 
                color='yellow', label='Bola')
        # Adicionando legenda
        plt.legend()
        # Definindo a cor do texto da legenda
        plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
        plt.legend().get_texts()[1].set_color("yellow")  # Bola em amarelo
        # Adicionando texto com o tempo de interceptação
        ax.set_xlabel('Tempo (s)')
        ax.set_ylabel('Posição Y (m)')
        ax.set_title('Trajetória do Robô e da Bola no eixo Y em Função do Tempo')
        plt.show()

    elif opcao == 4:
        ...

    elif opcao == 5:
        ...
    elif opcao == 6:
        ...
    elif opcao == 7:
        ...
    elif opcao == 8:
        ...

    elif opcao == 0:
        print()
        print("Saindo...")
        break