from tkinter import *
import principal
import funcoes
# import tkinter as tk

fontTexto = ("Arial", "12")
fontTitulo = ("Calibri", "15", "italic")

class menu_inicial:
    def __init__(self, master=None):        
        # Widget principal
        self.app = Frame(master)
        self.app.pack()
        
        
        # Menu Principal
        self.menu = Frame(self.app)
        self.menu["padx"] = 50
        self.menu.pack()
        
        self.titulo = Label(self.menu, text = "Projeto Ora Bolas!")
        self.titulo["font"] = fontTitulo
        self.titulo.pack()
        
        self.msg = Label(self.menu, text = "Digite a posição do Robô:")
        self.msg["font"] = fontTexto
        self.msg.pack()
        
        # Container dos dados digitados
        self.contDados = Frame(self.menu)
        self.contDados["pady"] = 20
        self.contDados.pack()
        
        # Container dos dados de X do robô
        self.contX = Frame(self.contDados)
        self.contX["pady"] = 5
        self.contX.pack()
        
        self.labelX = Label(self.contX, text = "X:")
        self.labelX["font"] = fontTexto
        self.labelX.pack(side = LEFT)
        
        self.posX = Entry(self.contX)
        self.posX["width"] = 20
        self.posX["font"] = fontTexto
        self.posX.pack()
        
        # Container dos dados de Y do robô
        self.contY = Frame(self.contDados)
        self.contY["pady"] = 5
        self.contY.pack(side = LEFT)
        
        self.labelY = Label(self.contY, text = "Y:")
        self.labelY["font"] = fontTexto
        self.labelY.pack(side = LEFT)
        
        self.posY = Entry(self.contY)
        self.posY["width"] = 20
        self.posY["font"] = fontTexto
        self.posY.pack(side = LEFT)

        # Container dos botões do menu principal
        self.contButton = Frame(self.menu)
        self.contButton["pady"] = 15
        self.contButton.pack()
        
        self.incio = Button(self.contButton)
        self.incio["text"] = "Iniciar"
        self.incio["font"] = fontTexto
        self.incio["width"] = 8
        self.incio["command"] = self.colectPos
        self.incio.pack()
        
        self.textRetorno = Label(self.menu, text = "", font = fontTexto)
        self.textRetorno.pack()
        
        
        # Menu de Opções
        self.options = Frame(self.app)
        self.options["pady"] = 10
        self.options.pack()
        
        self.sair = Button(self.options)
        self.sair["text"] = "Sair"
        self.sair["font"] = fontTexto
        self.sair["width"] = 8
        self.sair["command"] = self.app.quit
        self.sair.pack()
        
        pass
    
    def colectPos(self):
        posX = self.posX.get()
        try:
            posX = float(posX)
        except:
            self.textRetorno["text"] = "Digite somente Números"
            return
            
        posY = self.posY.get()
        try:
            posY = float(posY)
        except:
            self.textRetorno["text"] = "Digite somente Números"
            return
        
        print("X = ", posX, " Y = ", posY)
        
        funcoes.armazen_xy_robo(posX, posY)
        principal.inicio_programa()
        self.app.destroy() 
        menu_principal()
    

class menu_principal:
    def __init__(self, master = None):
        self.app = Frame(master)
        self.app.pack()
        
        
        self.titulo = Label(self.app, text = "Projeto Ora Bolas!")
        self.titulo["font"] = fontTitulo
        self.titulo.pack()
        
        self.msg = Label(self.app, text = "Selecione o Gráfico que deseja visualizar")
        self.msg["font"] = fontTitulo
        self.msg.pack()
        
        # Menu dos gráficos
        self.menu = Frame(self.app)
        self.menu.pack()

        self.row_index = 0
        
        # Posição
        self.text_posicoes = Label(self.menu, text = "Gráficos de posição")
        self.text_posicoes["font"] = fontTitulo
        self.text_posicoes.grid(row = self.row_index, columnspan = 2, pady = 10)
        
        self.row_index += 1
        
        # Gráfico da trajetória em X e Y entre o robô e a bola.
        self.text_1 = Label(self.menu, text = "Gráfico da trajetória em X e Y")
        self.text_1["font"] = fontTexto
        self.text_1.grid(row = self.row_index, column = 0, padx = 15, sticky = 'w')
        
        self.grafico1 = Button(self.menu)
        self.grafico1["text"] = "Abrir"
        self.grafico1["font"] = fontTexto
        self.grafico1["width"] = 8
        self.grafico1["command"] = principal.grafico1
        self.grafico1.grid(row = self.row_index, column = 1, padx = 15, sticky = 'e')
        
        self.row_index += 1
        
        # Gráfico da posição em X.        
        self.text_2 = Label(self.menu, text = "Gráfico da posição em X")
        self.text_2["font"] = fontTexto
        self.text_2.grid(row = self.row_index, column = 0, padx = 15, sticky = 'w')
        
        self.grafico2 = Button(self.menu)
        self.grafico2["text"] = "Abrir"
        self.grafico2["font"] = fontTexto
        self.grafico2["width"] = 8
        self.grafico2["command"] = principal.grafico2
        self.grafico2.grid(row = self.row_index, column = 1, padx = 15, sticky = 'e')
        
        self.row_index += 1
        
        # Gráfico da posicão em Y do robô e a bola.
        self.text_3 = Label(self.menu, text = "Gráfico da posição em Y")
        self.text_3["font"] = fontTexto
        self.text_3.grid(row = self.row_index, column = 0, padx = 15, sticky = 'w')
        
        self.grafico3 = Button(self.menu)
        self.grafico3["text"] = "Abrir"
        self.grafico3["font"] = fontTexto
        self.grafico3["width"] = 8
        self.grafico3["command"] = principal.grafico3
        self.grafico3.grid(row = self.row_index, column = 1, padx = 15, sticky = 'e')
        
        self.row_index += 1
        
        # Gráfico da distância entre o robô e a bola.
        self.text_4 = Label(self.menu, text = "Gráfico da distancia entre o robô e a bola")
        self.text_4["font"] = fontTexto
        self.text_4.grid(row = self.row_index, column = 0, padx = 15, sticky = 'w')
        
        self.grafico4 = Button(self.menu)
        self.grafico4["text"] = "Abrir"
        self.grafico4["font"] = fontTexto
        self.grafico4["width"] = 8
        self.grafico4["command"] = principal.grafico4
        self.grafico4.grid(row = self.row_index, column = 1, padx = 15, sticky = 'e')
        
        self.row_index += 1
        
        
        # Velocidade
        self.text_posicoes = Label(self.menu, text = "Gráficos de velocidade")
        self.text_posicoes["font"] = fontTitulo
        self.text_posicoes.grid(row = self.row_index, columnspan = 2, pady = 10)
        
        self.row_index += 1
        
        # Gráfico da Velocidade em X do robô e a bola.
        self.text_5 = Label(self.menu, text = "Gráfico da velocidade em X")
        self.text_5["font"] = fontTexto
        self.text_5.grid(row = self.row_index, column = 0, padx = 15, sticky = 'w')
        
        self.grafico5 = Button(self.menu)
        self.grafico5["text"] = "Abrir"
        self.grafico5["font"] = fontTexto
        self.grafico5["width"] = 8
        self.grafico5["command"] = principal.grafico5
        self.grafico5.grid(row = self.row_index, column = 1, padx = 15, sticky = 'e')
        
        self.row_index += 1
        
        # Gráfico da velocidade em Y do robô e a bola.
        self.text_6 = Label(self.menu, text = "Gráfico da velocidade em Y")
        self.text_6["font"] = fontTexto
        self.text_6.grid(row = self.row_index, column = 0, padx = 15, sticky = 'w')
        
        self.grafico6 = Button(self.menu)
        self.grafico6["text"] = "Abrir"
        self.grafico6["font"] = fontTexto
        self.grafico6["width"] = 8
        self.grafico6["command"] = principal.grafico6
        self.grafico6.grid(row = self.row_index, column = 1, padx = 15, sticky = 'e')
        
        self.row_index += 1
        
        
        # Aceleração
        self.text_posicoes = Label(self.menu, text = "Gráficos de aceleração")
        self.text_posicoes["font"] = fontTitulo
        self.text_posicoes.grid(row = self.row_index, columnspan = 2, pady = 10)
        
        self.row_index += 1
        
        # Gráfico da aceleração em X do robo e a bola.
        self.text_7 = Label(self.menu, text = "Gráfico da aceleração em X")
        self.text_7["font"] = fontTexto
        self.text_7.grid(row = self.row_index, column = 0, padx = 15, sticky = 'w')
        
        self.grafico7 = Button(self.menu)
        self.grafico7["text"] = "Abrir"
        self.grafico7["font"] = fontTexto
        self.grafico7["width"] = 8
        self.grafico7["command"] = principal.grafico7
        self.grafico7.grid(row = self.row_index, column = 1, padx = 15, sticky = 'e')
        
        self.row_index += 1
        
        # Gráfico da aceleração em Y do robo e a bola.
        self.text_8 = Label(self.menu, text = "Gráfico da aceleração em Y")
        self.text_8["font"] = fontTexto
        self.text_8.grid(row = self.row_index, column = 0, padx = 15, sticky = 'w')
        
        self.grafico8 = Button(self.menu)
        self.grafico8["text"] = "Abrir"
        self.grafico8["font"] = fontTexto
        self.grafico8["width"] = 8
        self.grafico8["command"] = principal.grafico8
        self.grafico8.grid(row = self.row_index, column = 1, padx = 15, sticky = 'e')
        
        
        # Menu de opções
        self.options = Frame(self.app)
        self.options["pady"] = 10
        self.options.pack()
        
        self.voltar = Button(self.options)
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = fontTexto
        self.voltar["width"] = 8
        self.voltar["command"] = self.voltar_func
        self.voltar.pack(side = LEFT, padx = 5)
        
        self.sair = Button(self.options)
        self.sair["text"] = "Sair"
        self.sair["font"] = fontTexto
        self.sair["width"] = 8
        self.sair["command"] = self.app.quit
        self.sair.pack(side = RIGHT, padx = 5)
         
    def voltar_func(self):
        self.app.destroy()
        menu_inicial()



# lista_tempo = []

# #pontos_da_bola
# pontos_em_x_da_posicao_bola = []
# pontos_em_y_da_posicao_bola = []
# #pontos_em_x_da_velocidade_bola = []
# #pontos_em_y_da_velocidade_bola = []
# #pontos_em_x_da_aceleracao_bola = []
# #pontos_em_y_da_aceleracao_bola = []

# #pontos do robô
# pontos_em_x_da_posicao_robo = []
# pontos_em_y_da_posicao_robo = []
# interceptacoes_x = []
# interceptacoes_y = []
# #pontos_em_x_da_velocidade_robo = []
# #pontos_em_y_da_velocidade_robo = []
# #pontos_em_x_da_aceleracao_robo = []
# #pontos_em_y_da_aceleracao_robo = []


# # GRÁFICO DE INTERCEPTAÇÃO DO ROBÔ EM X E Y.

# #funcão que armazena os pontos da bola em x e y.
# funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_da_bola_em_x, pontos_em_x_da_posicao_bola)
# funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_da_bola_em_y, pontos_em_y_da_posicao_bola)

# #função que armazena os pontos do robo em x e y.
# funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_robo_x,pontos_em_x_da_posicao_robo)
# funcoes.return_pontos_exatos_da_funcao(funcoes.posicao_robo_y, pontos_em_y_da_posicao_robo)

# #função do raio de interceptação
# funcoes.raio_de_interceptação(pontos_em_x_da_posicao_robo, pontos_em_x_da_posicao_bola, 
# pontos_em_y_da_posicao_robo,pontos_em_y_da_posicao_bola, interceptacoes_x, interceptacoes_y)

# #variável que pega o tempo em que o robô e a bola se encontram.
# tempo_interceptacao = funcoes.tempo_robo(interceptacoes_x)

# #Adicionando os intervalos de tempo a lista_tempo
# funcoes.return_tempo(lista_tempo)




# while True:
#     print("Digite o gráfico que deseja ver: ")
#     print('''
#           1 --> Gráfico da trajetória em X e Y entre o robô e a bola.
#           2 --> Gráfico da posição em X do robô e a bola.
#           3 --> Gráfico da posicão em Y do robô e a bola.
#           4 --> Gráfico da Velocidade em X do robô e a bola.
#           5 --> Gráfico da velocidade em Y do robô e a bola.
#           6 --> Gráfico da aceleração em X do robo e a bola.
#           7 --> Gráfico da aceleração em Y do robo e a bola.
#           8 --> Gráfico da distância entre o robô e a bola.
#           0 --> Sair.''')
#     opcao = int(input("Opção: "))

#     print()
#     if opcao == 1:
#         # Gráfico de interceptação entre o robô e a bola
#         fig, ax = plt.subplots()  
#         # Plotagem dos dados com diferentes cores
#         plt.plot(interceptacoes_x, interceptacoes_y,color='blue', label='Robô', )
#         plt.plot(pontos_em_x_da_posicao_bola, pontos_em_y_da_posicao_bola,
#                  color='yellow', label='Bola', )
#         plt.scatter(interceptacoes_x[-1],interceptacoes_y[-1], 
#                     color='green', label='Ponto de Encontro', s=20)
#         # Adicionando legenda
#         plt.legend()
#         # Definindo a cor do texto da legenda
#         plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
#         plt.legend().get_texts()[1].set_color("yellow")  # Bola em amarelo
#         plt.legend().get_texts()[2].set_color("green")
#         plt.text(0.001, 4.2, f'Tempo: {tempo_interceptacao} s', fontsize=12, color='black')
#         ax.set_xlabel('X(m)')
#         ax.set_ylabel('Y(m)')
#         ax.set_title('Gráfico da interceptação entre o robô e a bola')
#         plt.show()

#     elif opcao == 2:
#         # Gráfico da trajetória do robô e da bola em função do tempo
#         fig, ax = plt.subplots()  
#         # Plotagem dos dados com diferentes cores
#         plt.plot(lista_tempo[0:len(interceptacoes_x)], 
#                  pontos_em_x_da_posicao_robo[0:len(interceptacoes_x)], 
#                 color='blue', label='Robô')
#         plt.plot(lista_tempo[0:len(interceptacoes_x)],
#                   pontos_em_x_da_posicao_bola[0:len(interceptacoes_x)], 
#                 color='yellow', label='Bola')
#         # Adicionando legenda
#         plt.legend()
#         # Definindo a cor do texto da legenda
#         plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
#         plt.legend().get_texts()[1].set_color("yellow")  # Bola em amarelo
#         # Adicionando texto com o tempo de interceptação
#         ax.set_xlabel('Tempo (s)')
#         ax.set_ylabel('Posição X (m)')
#         ax.set_title('Trajetória do Robô e da Bola no eixo X em Função do Tempo')
#         plt.show()

#     elif opcao == 3:
#         # Gráfico da trajetória do robô e da bola em função do tempo
#         fig, ax = plt.subplots()  
#         # Plotagem dos dados com diferentes cores
#         plt.plot(lista_tempo[0:len(interceptacoes_y)], 
#                  pontos_em_y_da_posicao_robo[0:len(interceptacoes_y)], 
#                 color='blue', label='Robô')
#         plt.plot(lista_tempo[0:len(interceptacoes_y)], 
#                  pontos_em_y_da_posicao_bola[0:len(interceptacoes_y)], 
#                 color='yellow', label='Bola')
#         # Adicionando legenda
#         plt.legend()
#         # Definindo a cor do texto da legenda
#         plt.legend().get_texts()[0].set_color("blue")  # Robô em azul
#         plt.legend().get_texts()[1].set_color("yellow")  # Bola em amarelo
#         # Adicionando texto com o tempo de interceptação
#         ax.set_xlabel('Tempo (s)')
#         ax.set_ylabel('Posição Y (m)')
#         ax.set_title('Trajetória do Robô e da Bola no eixo Y em Função do Tempo')
#         plt.show()

#     elif opcao == 4:
#         ...
#     elif opcao == 5:
#         ...
#     elif opcao == 6:
#         ...
#     elif opcao == 7:
#         ...
#     elif opcao == 8:
#         ...

#     elif opcao == 0:
#         print()
#         print("Saindo...")
#         break

root = Tk()
root.title("Projeto Ora Bolas!")
menu_inicial(root)
# menu_principal(root)
root.mainloop()