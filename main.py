from tkinter import *
import principal
import funcoes
# import random

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
        
        # posX = round(random.uniform(0, 2), 3)
        # posY = round(random.uniform(0, 1.5), 3)
        # print("X: ",posX, "  Y: ", posY)
        
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


root = Tk()
root.title("Projeto Ora Bolas!")
menu_inicial(root)
# menu_principal(root)
root.mainloop()