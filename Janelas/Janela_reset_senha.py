import tkinter as tk
from Utilidades.Centralizar_janela import centralizar_janela
from Estilos.estilos import carregar_tema

def janela_resetar_senha(janela: tk.Tk):
    janela_reset = tk.Toplevel(janela)
    janela_reset.title("Esqueci a senha")
    centralizar_janela(janela_reset, 500, 400)
    tema = carregar_tema("Light")
    janela_reset.configure(bg=tema["cor_bg1"])

    tk.Label(janela_reset, text="Recuperação de senha", font=tema["fonte_titulo"], bg=tema["cor_bg2"]).pack(pady=10)

    tk.Label(janela_reset, text="Digite o seu usuário:", font=tema["fonte_texto"], bg=tema["cor_bg2"]).pack(pady=10)
    entrada_usuario = tk.Entry(janela_reset, font=tema["fonte_texto"], width=25)
    entrada_usuario.pack(pady=5)
    