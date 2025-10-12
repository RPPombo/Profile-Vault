import tkinter as tk
from Utilidades.Centralizar_janela import centralizar_janela
from Utilidades.Verificar_login import verificar_login
from Janela_contas import janela_contas
from Estilos.estilos import *

# -----Botão-----
def tentar_login(entrada_usuario: tk.Entry, entrada_senha: tk.Entry, janela: tk.Tk):
    usuario_dado = entrada_usuario.get()
    senha_dada = entrada_senha.get()

    if verificar_login(usuario_dado, senha_dada):
        janela.destroy()
        janela_contas(usuario_dado)
    else:
        aviso_login["text"] = "Usuário e/ou Senha incorreto(s)!"
        aviso_login["fg"] = "red"


# -----Elementos da janela-----
def criar_widgets_login(janela: tk.Tk):
    janela.configure(bg=cor_branco1)

    # Frame principal centralizado
    frame = tk.Frame(janela, bg=cor_branco2, padx=30, pady=30, relief="raised", bd=2)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Titulo
    tk.Label(frame, text="Login", font=fonte_titulo, bg=cor_branco2).pack(pady=(0, 20))

    # Entrada Usuário
    tk.Label(frame, text="Usuário:", font=fonte_texto, bg=cor_branco2).pack(pady=(5, 2))
    entrada_usuario = tk.Entry(frame, width=25, font=fonte_texto, bd=2, relief="groove")
    entrada_usuario.pack(pady=(0, 10))

    # Entrada Senha
    tk.Label(frame, text="Senha:", font=fonte_texto, bg=cor_branco2).pack(pady=(5, 2))
    entrada_senha = tk.Entry(frame, show="*", width=25, font=fonte_texto, bd=2, relief="groove")
    entrada_senha.pack(pady=(0, 20))

    # Botão Entrar
    botao = tk.Button(frame, text="Entrar", font=fonte_texto, bg=cor_verde1, fg="white",
                      activebackground=cor_verde2, width=15,
                      command=lambda: tentar_login(entrada_usuario, entrada_senha, janela))
    botao.pack(pady=(0, 10))

    # Label de aviso de login
    global aviso_login
    aviso_login = tk.Label(frame, text="", font=fonte_texto, bg=cor_branco2)
    aviso_login.pack(pady=(0, 5))

# -----Criar janela-----
def janela_login():
    janela = tk.Tk()
    janela.title("Login")
    centralizar_janela(janela, 500, 450)
    criar_widgets_login(janela)
    janela.mainloop()
