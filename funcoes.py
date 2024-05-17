'''
Funções da bola com a variável tempo

função da posição 
--> X(t) = 0.005t³ -0.00000000000007t² +  0.5t+ 1
--> Y(t) = -0,02t² + 0,9t + 0,5

Função da velocidade
--> Vx(t) = 0,015t² -0,0003t + 0,5
--> Vy(t) = -0,04.t + 0,9004

 Função da aceleração
 --> Ax(t) = 0,03t - 0,0006
 --> Ay(t) = -0,04

'''





import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from math import sqrt;

aceleracao_robo_x = 2.8
aceleracao_robo_y = 2.8
X_inicial_bola = 1
Y_inicial_bola = 0.5

x_do_robo = -1
y_do_robo = -1

def armazen_xy_robo(x, y):
	global x_do_robo
	global y_do_robo
	global aceleracao_robo_y
	
	x_do_robo = x
	y_do_robo = y

	if x_do_robo < X_inicial_bola and y_do_robo > x_do_robo and y_do_robo > X_inicial_bola:
		aceleracao_robo_y = aceleracao_robo_y * (-1)





#Funções da bola
def posicao_da_bola_em_x(t=0):
	x = round(0.005 * t**3 - 0.000000000000007 * t**2 + 0.5*t + 1, 8)
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

def aceleracao_bola_x(t=0):
	Ax = 0.03*t - 0.0006
	return Ax

def aceleracao_bola_y(t=0):
	Ay = -0.04
	return Ay


#Funções do robô
def posicao_robo_x(t=0, aceleracao=aceleracao_robo_x):
	if x_do_robo > X_inicial_bola and y_do_robo < x_do_robo:
		aceleracao = aceleracao_robo_x * (-1)
	if y_do_robo < Y_inicial_bola and  x_do_robo < X_inicial_bola:
		aceleracao = 2.8
	x = round(x_do_robo + 0*t + (aceleracao * t**2)/2, 8)
	return x

def posicao_robo_y(t=0, aceleracao = aceleracao_robo_y):
	y = round(y_do_robo + 0*t + (aceleracao * t**2)/2, 6)
	return y

def posicao_robo_y_negativa(t=0):
	y = round(y_do_robo + 0*t + (-2.8 * t**2)/2, 6)
	return y

def Velocidade_robo_x(t=0):
	vx = round(0 + (2.8 * t) , 6)
	if vx > 2.8:
		vx = 2.8
	return vx

def velocidade_robo_y(t = 0):
	vy = round(0 + (2.8 * t) , 6)
	if vy > 2.8:
		vy = 2.8
	return vy

def aceleracao_robo(t=0):
	Ar = 2.8
	return Ar



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
def raio_de_interceptação(x_robo, x_bola, y_robo, y_bola, lista_x, lista_y, lista_distancia):
	for i in range(len(x_robo)):
		for j in range(len(x_bola)):
			distancia = sqrt((x_robo[i] - x_bola[j])**2 + (y_robo[i] - y_bola[j])**2)
			if distancia <= 0.1115:
				lista_distancia.append(distancia)
				return True
			else:
				if x_robo[i] in lista_x or y_robo[i] in lista_y:
					pass
				else:
					lista_x.append(x_robo[i])
					lista_y.append(y_robo[i])
					lista_distancia.append(distancia)

#função que lê o tempo de encontro entre o robo e a bola
def tempo_robo(interceptacoes_x):
	# O tempo é igual ao número de pontos de interceptação multiplicado pelo intervalo de tempo (0.02)
	tempo = len(interceptacoes_x) * 0.02
	return round(tempo, 2)

#GRÁFICOS SENDO CRIADOS ABAIXO: 

def grafico_trajetoria_XY(listax_robo, listay_robo, listax_bola, listay_bola, tempo_interceptacao):
		# Gráfico de interceptação entre o robô e a bola em XY
		fig, ax = plt.subplots()  
		# Plotagem dos dados com diferentes cores
		plt.plot(listax_robo, listay_robo,color='blue', label='Robô', )
		plt.plot(listax_bola, listay_bola,
				 color='orange', label='Bola', )
		plt.scatter(listax_robo[-1], listay_robo[-1], 
					color='black', label='Ponto de Encontro', s=20)
		# Adicionando legenda
		plt.legend()
		# Definindo a cor do texto da legenda
		plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
		plt.legend().get_texts()[1].set_color("orange")  # Bola em amarelo
		plt.legend().get_texts()[2].set_color("black")
		plt.text(0.021, 4.1, f'Tempo: {tempo_interceptacao} s', fontsize=12, color='black')
		ax.set_xlabel('X(m)')
		ax.set_ylabel('Y(m)')
		ax.set_title('Gráfico da interceptação entre o robô e a bola')
		plt.show()

def grafico_trajetoria_X(interceptacoes_x, pontos_em_x_da_posicao_bola, lista_tempo):
		# Gráfico da trajetória do robô e da bola em X em função do tempo
		fig, ax = plt.subplots()  
		# Plotagem dos dados com diferentes cores
		plt.plot(lista_tempo[0:len(interceptacoes_x)], 
				 interceptacoes_x, 
				color='blue', label='Robô')
		plt.plot(lista_tempo[0:len(interceptacoes_x)],
				  pontos_em_x_da_posicao_bola[0:len(interceptacoes_x)], 
				color='orange', label='Bola')
		# Adicionando legenda
		plt.legend()
		# Definindo a cor do texto da legenda
		plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
		plt.legend().get_texts()[1].set_color("orange")  # Bola em amarelo
		ax.set_xlabel('Tempo (s)')
		ax.set_ylabel('Posição X (m)')
		ax.set_ylim(0, 9)
		ax.set_title('Trajetória do Robô e da Bola no eixo X em Função do Tempo')
		plt.show()

def grafico_trajetoria_Y(interceptacoes_y, pontos_em_y_da_posicao_bola, lista_tempo):
		# Gráfico da trajetória do robô em Y e da bola em função do tempo
		fig, ax = plt.subplots()  
		# Plotagem dos dados com diferentes cores
		plt.plot(lista_tempo[0:len(interceptacoes_y)], 
				 interceptacoes_y, 
				color='blue', label='Robô')
		plt.plot(lista_tempo[0:len(interceptacoes_y)], 
				 pontos_em_y_da_posicao_bola[0:len(interceptacoes_y)], 
				color='orange', label='Bola')
		# Adicionando legenda
		plt.legend()
		# Definindo a cor do texto da legenda
		plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
		plt.legend().get_texts()[1].set_color("orange")  # Bola em amarelo
		ax.set_xlabel('Tempo (s)')
		ax.set_ylabel('Posição Y (m)')
		ax.set_ylim(0, 6)
		ax.set_title('Trajetória do Robô e da Bola no eixo Y em Função do Tempo')
		plt.show()

def grafico_trajetoria_Y_negativo(interceptacoes_y_negativo, pontos_em_y_da_posicao_bola, lista_tempo):
	# Gráfico da trajetória do robô em Y e da bola em função do tempo
		fig, ax = plt.subplots()  
		# Plotagem dos dados com diferentes cores
		plt.plot(lista_tempo[0:len(interceptacoes_y_negativo)], 
				 interceptacoes_y_negativo, 
				color='blue', label='Robô')
		plt.plot(lista_tempo[0:len(interceptacoes_y_negativo)], 
				 pontos_em_y_da_posicao_bola[0:len(interceptacoes_y_negativo)], 
				color='orange', label='Bola')
		# Adicionando legenda
		plt.legend()
		# Definindo a cor do texto da legenda
		plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
		plt.legend().get_texts()[1].set_color("orange")  # Bola em amarelo
		ax.set_xlabel('Tempo (s)')
		ax.set_ylabel('Posição Y (m)')
		ax.set_ylim(0, 6)
		ax.set_title('Trajetória do Robô e da Bola no eixo Y em Função do Tempo')
		plt.show()

def grafico_velocidade_X(pontos_em_x_da_velocidade_robo, interceptacoes_x, 
				 pontos_em_x_da_velocidade_bola, lista_tempo):
		# Gráfico da velocidade do robô e da bola  em X e em função do tempo
		fig, ax = plt.subplots()  
		# Plotagem dos dados com diferentes cores
		plt.plot(lista_tempo[0:len(interceptacoes_x)], 
				 pontos_em_x_da_velocidade_robo[0:len(interceptacoes_x)], 
				color='blue', label='Robô')
		plt.plot(lista_tempo[0:len(interceptacoes_x)], 
				 pontos_em_x_da_velocidade_bola[0:len(interceptacoes_x)], 
				color='orange', label='Bola')
		# Adicionando legenda
		plt.legend()
		# Definindo a cor do texto da legenda
		plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
		plt.legend().get_texts()[1].set_color("orange")  # Bola em amarelo
		ax.set_xlabel('Tempo (s)')
		ax.set_ylabel('Velocidade X(m)')
		ax.set_title('Velocidade do robô e bola em função do tempo no eixo X')
		plt.yticks(np.arange(-1, 3, 0.5))
		plt.show()

def grafico_velocidade_Y(pontos_em_y_da_velocidade_robo, interceptacoes_y,
				pontos_em_y_da_velocidade_bola, lista_tempo):
		#Gráfico da velocidade  do robô e da bola em Y em função do tempo
		fig, ax = plt.subplots()  
		# Plotagem dos dados com diferentes cores
		plt.plot(lista_tempo[0:len(interceptacoes_y)], 
				 pontos_em_y_da_velocidade_robo[0:len(interceptacoes_y)], 
				color='blue', label='Robô')
		plt.plot(lista_tempo[0:len(interceptacoes_y)], 
				 pontos_em_y_da_velocidade_bola[0:len(interceptacoes_y)], 
				color='orange', label='Bola')
		# Adicionando legenda
		plt.legend()
		# Definindo a cor do texto da legenda
		plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
		plt.legend().get_texts()[1].set_color("orange")  # Bola em amarelo
		ax.set_xlabel('Tempo (s)')
		ax.set_ylabel('Velocidade Y(m)')
		ax.set_title('Velocidade do robô e bola em  função do tempo no eixo Y')
		plt.yticks(np.arange(-1, 3, 0.5))
		plt.show()

def grafico_aceleracao_X(pontos_em_x_da_aceleracao_robo, interceptacoes_x,
				 pontos_em_x_da_aceleracao_bola, lista_tempo):

		#Gráfico da Aceleração do robô e da bola em função do tempo
		fig, ax = plt.subplots()  
		# Plotagem dos dados com diferentes cores
		plt.plot(lista_tempo[0:len(interceptacoes_x)], 
				 pontos_em_x_da_aceleracao_robo[0:len(interceptacoes_x)], 
				color='blue', label='Robô')
		plt.plot(lista_tempo[0:len(interceptacoes_x)], 
				 pontos_em_x_da_aceleracao_bola[0:len(interceptacoes_x)], 
				color='orange', label='Bola')
		# Adicionando legenda
		plt.legend()
		# Definindo a cor do texto da legenda
		plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
		plt.legend().get_texts()[1].set_color("orange")  # Bola em amarelo
		ax.set_xlabel('Tempo (s)')
		ax.set_ylabel('Aceleração X(m)')
		ax.set_title('Aceleração do robô e bola em  função do tempo no eixo X')
		#definindo começo, fim, intervalo no eixo Y.
		plt.yticks(np.arange(-1, 3, 0.2))
		plt.show()

def grafico_aceleracao_Y(pontos_em_y_da_aceleracao_robo, interceptacoes_y,
				pontos_em_y_da_aceleracao_bola, lista_tempo):
		#Gráfico da aceleração do robô e da bola em função do tempo no eixo Y
		fig, ax = plt.subplots()  
		# Plotagem dos dados com diferentes cores
		plt.plot(lista_tempo[0:len(interceptacoes_y)], 
				 pontos_em_y_da_aceleracao_robo[0:len(interceptacoes_y)], 
				color='blue', label='Robô')
		plt.plot(lista_tempo[0:len(interceptacoes_y)], 
				 pontos_em_y_da_aceleracao_bola[0:len(interceptacoes_y)], 
				color='orange', label='Bola')
		# Adicionando legenda
		plt.legend()
		# Definindo a cor do texto da legenda
		plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
		plt.legend().get_texts()[1].set_color("orange")  # Bola em amarelo
		ax.set_xlabel('Tempo (s)')
		ax.set_ylabel('Aceleração Y(m)')
		ax.set_title('Aceleração do robô e bola em  função do tempo no eixo Y')
		#definindo começo, fim, intervalo no eixo Y.
		plt.yticks(np.arange(-1, 3, 0.2))
		plt.show()

def grafico_distancia(distancia, lista_tempo):
		fig, ax = plt.subplots()  
		# Plotagem dos dados com diferentes cores
		plt.plot(lista_tempo[0:len(distancia)], 
				 distancia,
				color='red', label='Distância')
		# Adicionando legenda
		plt.legend()
		# Definindo a cor do texto da legenda
		plt.legend().get_texts()[0].set_color("red")  # Distância em azul
		ax.set_xlabel('Tempo (s)')
		ax.set_ylabel('Distância (m)')
		ax.set_title('Distância entre o robô e  bola em função do tempo')
		plt.show()


def vetor_velocidade(origemXRobo, origemYRobo, finalXRobo, 
					 finalYRobo, origemXbola, origemYbola,
					   finalXbola, finalYbola, moduloR, moduloB):
	fig, ax = plt.subplots()
	ax.quiver(origemXRobo, origemYRobo, finalXRobo, finalYRobo,
		    angles='xy', scale_units='xy', scale=1, color='blue', 
			label=f'Vetor Velocidade Robo (Módulo: {moduloR})')
	ax.quiver(origemXbola, origemYbola, finalXbola, finalYbola, angles='xy',
		    scale_units='xy', scale=1, color='orange', 
			label=f'Vetor Velocidade bola (Módulo: {moduloB})')
	# Configuração dos eixos
	ax.set_xlim([-1, 4])
	ax.set_ylim([-2, 3])

	# Adição de rótulos e título
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_title('Vetores Velocidade')

	ax.set_xlim([-1, 4])
	ax.set_ylim([-2, 4])

	# Exibição do gráfico
	plt.legend()
	plt.grid()
	plt.show()

def vetor_aceleracao(origemXRobo, origemYRobo, finalXRobo, finalYRobo, origemXbola, origemYbola, finalXbola, finalYbola):
	fig, ax = plt.subplots()
	ax.quiver(origemXRobo, origemYRobo, finalXRobo, finalYRobo, angles='xy', scale_units='xy', scale=1, color='blue', label='Vetores do Robô')
	ax.quiver(origemXbola, origemYbola, finalXbola, finalYbola, angles='xy', scale_units='xy', scale=1, color='orange', label='Vetores da Bola')
	# Configuração dos eixos
	ax.set_xlim([-1, 10])
	ax.set_ylim([-2, 10])

	# Adição de rótulos e título
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_title('Vetores Aceleração')

	# Exibição do gráfico
	plt.legend()
	plt.grid()
	plt.show()

def modulo_vetor(finalX, finalY):
    modulo = round(np.sqrt(np.array(finalX)**2 + np.array(finalY)**2), 2)
    return modulo






	 






