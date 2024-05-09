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
pontos_em_x_da_aceleracao_bola = []
pontos_em_y_da_aceleracao_bola = []

#pontos do robô
pontos_em_x_da_posicao_robo = []
pontos_em_y_da_posicao_robo = []
interceptacoes_x = []
interceptacoes_y = []
pontos_em_x_da_velocidade_robo = []
pontos_em_y_da_velocidade_robo = []
pontos_em_x_da_aceleracao_robo = []
pontos_em_y_da_aceleracao_robo = []


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

#GRÁFICO PARA VELOCIDADE DO ROBÔ E BOLA EM X E Y

#Armazenando os pontos da velocidade da bola em X e Y.
funcoes.return_pontos_exatos_da_funcao(funcoes.velocidade_bola_x, 
pontos_em_x_da_velocidade_bola)
funcoes.return_pontos_exatos_da_funcao(funcoes.velocidade_bola_y,
pontos_em_y_da_velocidade_bola)

#Armazenando os pontos da velocidade do robô em X e Y.
funcoes.return_pontos_exatos_da_funcao(funcoes.Velocidade_robo_x, 
pontos_em_x_da_velocidade_robo)
funcoes.return_pontos_exatos_da_funcao(funcoes.velocidade_robo_y,
pontos_em_y_da_velocidade_robo)


#GRÁFICO PARA ACELERAÇÃO DO ROBÔ E BOLA EM X E Y
#armazenandos os pontos da aceleração da bola.
funcoes.return_pontos_exatos_da_funcao(funcoes.aceleracao_bola_x,
pontos_em_x_da_aceleracao_bola)
funcoes.return_pontos_exatos_da_funcao(funcoes.aceleracao_bola_y,
pontos_em_y_da_aceleracao_bola)

#armazenando os pontos da aceleração do robô:
funcoes.return_pontos_exatos_da_funcao(funcoes.aceleracao_robo,
pontos_em_x_da_aceleracao_robo)
funcoes.return_pontos_exatos_da_funcao(funcoes.aceleracao_robo,
pontos_em_y_da_aceleracao_robo)


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
        funcoes.grafico_trajetoria_XY(interceptacoes_x, interceptacoes_y, pontos_em_x_da_posicao_bola,
                              pontos_em_y_da_posicao_bola, tempo_interceptacao)
        

    elif opcao == 2:
        funcoes.grafico_trajetoria_X(interceptacoes_x, pontos_em_x_da_posicao_bola, 
                            lista_tempo)
        

    elif opcao == 3:
        funcoes.grafico_trajetoria_Y(interceptacoes_y, pontos_em_y_da_posicao_bola,
                             lista_tempo)
        

    elif opcao == 4:
        funcoes.grafico_velocidade_X(pontos_em_x_da_velocidade_robo, interceptacoes_x, 
                             pontos_em_x_da_velocidade_bola, lista_tempo)
        

    elif opcao == 5:
        funcoes.grafico_velocidade_Y(pontos_em_y_da_velocidade_robo, interceptacoes_y,
                             pontos_em_y_da_velocidade_bola, lista_tempo)
        

    elif opcao == 6:
        funcoes.grafico_aceleracao_X(pontos_em_x_da_aceleracao_robo, interceptacoes_x,
                             pontos_em_x_da_aceleracao_bola, lista_tempo)
        

    elif opcao == 7:
        funcoes.grafico_aceleracao_Y(pontos_em_y_da_aceleracao_robo, interceptacoes_y,
                             pontos_em_y_da_aceleracao_bola, lista_tempo)


    elif opcao == 8:
        ...

    elif opcao == 0:
        print()
        print("Saindo...")
        break