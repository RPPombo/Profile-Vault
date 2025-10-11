import tkinter as tk

def centralizar_janela(janela: tk.Tk, largura: int, altura: int):
    # Conseguindo o tamanho da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calculando as coordenadas
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)

    # Aplicando as coordenadas
    janela.geometry(f"{largura}x{altura}+{x}+{y}")