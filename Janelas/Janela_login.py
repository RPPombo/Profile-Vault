import tkinter as tk
from Utilidades.Centralizar_janela import centralizar_janela
from Utilidades.Verificar_login import verificar_login

fonte_titulo = ("Times New Roman", 22, "bold")
fonte_texto = ("Times New Roman", 14)
cor_fundo = "#f0f0f0"
cor_frame = "#ffffff"
cor_botao = "#4CAF50"
cor_botao_hover = "#45a049"

def tentar_login(entrada_usuario: tk.Entry, entrada_senha: tk.Entry, janela: tk.Tk):
    usuario_dado = entrada_usuario.get()
    senha_dada = entrada_senha.get()

    if verificar_login(usuario_dado, senha_dada):
        janela.destroy()
        # aqui você pode abrir a próxima janela
    else:
        aviso_login["text"] = "Usuário e/ou Senha incorreto(s)!"
        aviso_login["fg"] = "red"

def criar_widgets(janela: tk.Tk):
    janela.configure(bg=cor_fundo)

    # Frame principal centralizado
    frame = tk.Frame(janela, bg=cor_frame, padx=30, pady=30, relief="raised", bd=2)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Titulo
    tk.Label(frame, text="Login", font=fonte_titulo, bg=cor_frame).pack(pady=(0, 20))

    # Entrada Usuário
    tk.Label(frame, text="Usuário:", font=fonte_texto, bg=cor_frame).pack(pady=(5, 2))
    entrada_usuario = tk.Entry(frame, width=25, font=fonte_texto, bd=2, relief="groove")
    entrada_usuario.pack(pady=(0, 10))

    # Entrada Senha
    tk.Label(frame, text="Senha:", font=fonte_texto, bg=cor_frame).pack(pady=(5, 2))
    entrada_senha = tk.Entry(frame, show="*", width=25, font=fonte_texto, bd=2, relief="groove")
    entrada_senha.pack(pady=(0, 20))

    # Botão Entrar
    botao = tk.Button(frame, text="Entrar", font=fonte_texto, bg=cor_botao, fg="white",
                      activebackground=cor_botao_hover, width=15,
                      command=lambda: tentar_login(entrada_usuario, entrada_senha, janela))
    botao.pack(pady=(0, 10))

    # Label de aviso de login
    global aviso_login
    aviso_login = tk.Label(frame, text="", font=fonte_texto, bg=cor_frame)
    aviso_login.pack(pady=(0, 5))

def janela_login():
    janela = tk.Tk()
    janela.title("Login")
    centralizar_janela(janela, 500, 450)
    criar_widgets(janela)
    janela.mainloop()
