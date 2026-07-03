import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox


def calcular():
    tk.Label(janela, text="Deu certo!").grid(row=6)


largura = 600
altura = 300

janela = tk.Tk()
janela.title("Método de Newton")
janela.geometry(f"{largura}x{altura}")

fonte = Font(
    family="Arial",
    size=22,
    weight="bold",     # "normal" ou "bold"
    slant="roman",     # "roman" ou "italic"
    underline=False,
    overstrike=False    
)

titulo = tk.Label(janela, text="Método de Newton", font=fonte)
titulo.grid(row=0)

# Coluna das entradas
tk.Label(janela, text="Índice (número natural maior que zero) [n]:").grid(row=1, column=0)
tk.Entry(janela).grid(row=2, column=0)

tk.Label(janela, text="Radical (número real) [A]:").grid(row=3, column=0)
tk.Entry(janela).grid(row=4, column=0)

tk.Button(janela, text="Enviar", width=10, command=calcular).grid(row=5, column=0)

# Coluna das saídas

# Rodapé
tk.Label(janela, text="Feito por Henrique Angelin e Evelyn Dantas.").grid(row=7)

janela.mainloop()
