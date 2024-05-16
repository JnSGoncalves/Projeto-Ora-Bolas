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
pontos_em_y_da_posicao_robo_negativos = []
interceptacoes_x = []
interceptacoes_y = []
#separando
interceptacoes_x_do_y_negativo = []
interceptacoes_y_negativo = []
# -----
pontos_em_x_da_velocidade_robo = []
pontos_em_y_da_velocidade_robo = []
pontos_em_x_da_aceleracao_robo = []
pontos_em_y_da_aceleracao_robo = []
distancia = []
distancia_y_negativo = []

tempo_interceptacao = 0

def inicio_programa():
	global lista_tempo

	#pontos_da_bola
	global pontos_em_x_da_posicao_bola
	global pontos_em_y_da_posicao_bola
	global pontos_em_x_da_velocidade_bola
	global pontos_em_y_da_velocidade_bola
	global pontos_em_x_da_aceleracao_bola
	global pontos_em_y_da_aceleracao_bola

	#pontos do robô
	global pontos_em_x_da_posicao_robo
	global pontos_em_y_da_posicao_robo
	global pontos_em_y_da_posicao_robo_negativos
	global interceptacoes_x
	global interceptacoes_y
	#separando
	global interceptacoes_x_do_y_negativo
	global interceptacoes_y_negativo
	# -----
	global pontos_em_x_da_velocidade_robo
	global pontos_em_y_da_velocidade_robo
	global pontos_em_x_da_aceleracao_robo
	global pontos_em_y_da_aceleracao_robo
	global distancia
	global distancia_y_negativo

	global tempo_interceptacao
	
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
	pontos_em_y_da_posicao_robo_negativos = []
	interceptacoes_x = []
	interceptacoes_y = []
	#separando
	interceptacoes_x_do_y_negativo = []
	interceptacoes_y_negativo = []
	# -----
	pontos_em_x_da_velocidade_robo = []
	pontos_em_y_da_velocidade_robo = []
	pontos_em_x_da_aceleracao_robo = []
	pontos_em_y_da_aceleracao_robo = []
	distancia = []
	distancia_y_negativo = []

	tempo_interceptacao = 0
	
	# GRÁFICO DE INTERCEPTAÇÃO DO ROBÔ EM X E Y.
	
	#funcão que armazena os pontos da bola em x e y.
	funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_da_bola_em_x, pontos_em_x_da_posicao_bola)
	funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_da_bola_em_y, pontos_em_y_da_posicao_bola)
	
	#função que armazena os pontos do robo em x e y.
	funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_robo_x,pontos_em_x_da_posicao_robo)
	funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_robo_y, pontos_em_y_da_posicao_robo)
	funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_robo_y_negativa, pontos_em_y_da_posicao_robo_negativos)
	
	#função do raio de interceptação com y positivo
	funcoes.raio_de_interceptação(pontos_em_x_da_posicao_robo, pontos_em_x_da_posicao_bola, 
	pontos_em_y_da_posicao_robo, pontos_em_y_da_posicao_bola, interceptacoes_x, interceptacoes_y,
	distancia)
	
	#função com raio de interceptação com y negativo
	funcoes.raio_de_interceptação(pontos_em_x_da_posicao_robo, pontos_em_x_da_posicao_bola, 
	pontos_em_y_da_posicao_robo_negativos, pontos_em_y_da_posicao_bola, interceptacoes_x_do_y_negativo, 
	interceptacoes_y_negativo, distancia_y_negativo)
	
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




def grafico1():
	funcoes.grafico_trajetoria_XY(interceptacoes_x, interceptacoes_y, pontos_em_x_da_posicao_bola,
						  pontos_em_y_da_posicao_bola, tempo_interceptacao)


def grafico2():
	funcoes.grafico_trajetoria_X(pontos_em_x_da_posicao_robo, pontos_em_x_da_posicao_bola, 
						lista_tempo)


def grafico3():
	if funcoes.y_do_robo > funcoes.Y_inicial_bola + 0.1:
		funcoes.grafico_trajetoria_Y_negativo(pontos_em_y_da_posicao_robo_negativos, 
		pontos_em_y_da_posicao_bola, lista_tempo)

	else:
		funcoes.grafico_trajetoria_Y(pontos_em_y_da_posicao_robo, 
		pontos_em_y_da_posicao_bola, lista_tempo)


def grafico4():
	funcoes.grafico_distancia(distancia, lista_tempo)


def grafico5():
	funcoes.grafico_velocidade_X(pontos_em_x_da_velocidade_robo, interceptacoes_x, 
						 pontos_em_x_da_velocidade_bola, lista_tempo)


def grafico6():
	funcoes.grafico_velocidade_Y(pontos_em_y_da_velocidade_robo, interceptacoes_y,
						 pontos_em_y_da_velocidade_bola, lista_tempo)


def grafico7():
	funcoes.grafico_aceleracao_X(pontos_em_x_da_aceleracao_robo, interceptacoes_x,
						 pontos_em_x_da_aceleracao_bola, lista_tempo)


def grafico8():
	funcoes.grafico_aceleracao_Y(pontos_em_y_da_aceleracao_robo, interceptacoes_y,
						 pontos_em_y_da_aceleracao_bola, lista_tempo)

def grafico9():
	funcoes.vetor_velocidade(pontos_em_x_da_velocidade_robo[0], pontos_em_y_da_velocidade_robo[0],
	pontos_em_x_da_velocidade_robo[-1], pontos_em_y_da_velocidade_robo[-1], pontos_em_x_da_velocidade_bola[0],
	pontos_em_y_da_velocidade_bola[0], pontos_em_x_da_velocidade_bola[-1], pontos_em_y_da_velocidade_bola[-1])

def grafico10():
	...