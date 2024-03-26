import tkinter as tk

def clique_botao():
    print("Botão clicado!")

print("Hello World!")

janela = tk.Tk()
janela.title("Minha Primeira Janela")


botao = tk.Button(janela, text="Clique Aqui", command=clique_botao)
botao.pack()

janela.mainloop()