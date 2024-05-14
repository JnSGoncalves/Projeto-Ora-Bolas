import tkinter as tk
from PIL import Image, ImageTk

# Funções de posição, velocidade e aceleração
def x(t):
    return 0.005 * t**3 - 7E-14 * t**2 + 0.5 * t + 1

def y(t):
    return -0.02 * t**2 + 0.9 * t + 0.5

# Função para atualizar a posição da bola
def update_position():
    global t, ball
    if t < 24:  # Limite de tempo para a animação
        canvas.move(ball, x(t) - x(t-1), y(t) - y(t-1))
        t += 0.1  # Incremento de tempo
        window.after(100, update_position)  # Chamada recursiva após 100ms

# Configurações da janela principal
window = tk.Tk()
window.title("Animação da Bola")

# Carregar a imagem do campo
campo_img = Image.open("./imagens/campo.jpg")
campo_img = campo_img.resize((900, 600))  # Redimensiona a imagem para o tamanho desejado
campo_img = ImageTk.PhotoImage(campo_img)

# Configurações do canvas com o campo de futebol como fundo
canvas = tk.Canvas(window, width=900, height=600)
canvas.create_image(0, 0, anchor=tk.NW, image=campo_img)
canvas.pack()

# Criação da bola no canvas
ball = canvas.create_oval(30, 30, 15, 15, fill="red")

# Variável de tempo
t = 0

# Inicia a animação
update_position()

# Inicia o loop principal do tkinter
window.mainloop()
