from tkinter import *
# import tkinter as tk

posX = None
posY = None

class Aplicacao:
    def __init__(self, master=None):
        self.fontTexto = ("Arial", "12")
        self.fontTitulo = ("Calibri", "15", "italic")
        
        # Widget principal
        self.app = Frame(master)
        self.app.pack()
        
        
        # Menu Principal
        self.menu = Frame(self.app)
        self.menu["padx"] = 50
        self.menu.pack()
        
        self.titulo = Label(self.menu, text = "Projeto Ora Bolas!")
        self.titulo["font"] = self.fontTitulo
        self.titulo.pack()
        
        self.msg = Label(self.menu, text = "Digite a posição do Robô:")
        self.msg["font"] = self.fontTexto
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
        self.labelX["font"] = self.fontTexto
        self.labelX.pack(side = LEFT)
        
        self.posX = Entry(self.contX)
        self.posX["width"] = 20
        self.posX["font"] = self.fontTexto
        self.posX.pack()
        
        # Container dos dados de Y do robô
        self.contY = Frame(self.contDados)
        self.contY["pady"] = 5
        self.contY.pack(side = LEFT)
        
        self.labelY = Label(self.contY, text = "Y:")
        self.labelY["font"] = self.fontTexto
        self.labelY.pack(side = LEFT)
        
        self.posY = Entry(self.contY)
        self.posY["width"] = 20
        self.posY["font"] = self.fontTexto
        self.posY.pack(side = LEFT)

        # Container dos botões do menu principal
        self.contButton = Frame(self.menu)
        self.contButton["pady"] = 15
        self.contButton.pack()
        
        self.incio = Button(self.contButton)
        self.incio["text"] = "Iniciar"
        self.incio["font"] = self.fontTexto
        self.incio["width"] = 8
        self.incio["command"] = self.colectPos
        self.incio.pack()
        
        self.textRetorno = Label(self.menu, text = "", font = self.fontTexto)
        self.textRetorno.pack()
        
        
        # Menu de Opções
        self.options = Frame(self.app)
        self.options["pady"] = 10
        self.options.pack()
        
        self.sair = Button(self.options)
        self.sair["text"] = "Sair"
        self.sair["font"] = self.fontTexto
        self.sair["width"] = 8
        self.sair["command"] = self.app.quit
        self.sair.pack()
        
        pass
    
    def colectPos(self):
        global posX
        global posY
        
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



root = Tk()
root.title("Projeto Ora Bolas!")
Aplicacao(root)
root.mainloop()