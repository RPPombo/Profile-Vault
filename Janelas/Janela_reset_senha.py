import tkinter as tk
from Utilidades.Centralizar_janela import centralizar_janela
from Estilos.estilos import *

def janela_resetar_senha(janela: tk.Tk):
    janela_reset = tk.Toplevel(janela)
    janela_reset.title("Esqueci a senha")
    centralizar_janela(janela_reset, 500, 400)
    janela_reset.configure(bg=cor_branco1)

    tk.Label(janela_reset, text="Recuperação de senha", font=fonte_titulo, bg=cor_branco2).pack(pady=10)

    tk.Label(janela_reset, text="Digite o seu usuário:", font=fonte_texto, bg=cor_branco2).pack(pady=10)
    entrada_usuario = tk.Entry(janela_reset, font=fonte_texto, width=25)
    entrada_usuario.pack(pady=5)
    