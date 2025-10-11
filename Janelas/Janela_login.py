import tkinter as tk
from Utilidades.Centralizar_janela import centralizar_janela
from Utilidades.Verificar_login import verificar_login

fonte_titulo = ("Times New Roman", 20)
fonte_texto = ("Times New Roman", 13)
login_liberado = False

def tentar_login(entrada_usuario: tk.Entry, entrada_senha: tk.Entry, janela: tk.Tk):
    usuario_dado = entrada_usuario.get()
    senha_dada = entrada_senha.get()

    if verificar_login(usuario_dado, senha_dada):
        janela.destroy()
        #janela_perfis = janela_perfis()
        #janela_perfis.mainloop()

    else:
        for widget in janela.winfo_children():
            widget.destroy()
        criar_widgets(janela)
        tk.Label(janela, text="Usuário e/ou Senha incorreto(s)!", font= fonte_texto, fg="red").pack(pady= 10)
        tk.Label(janela, text="Tente Novamente!", font= fonte_texto, fg="red").pack(pady= 10)

def criar_widgets(janela: tk.Tk) -> tk.Tk:
    # Titulo
    tk.Label(janela, text="Login", font= fonte_titulo, justify="center").pack(pady=20)

    # Entradas
    tk.Label(janela, text="Usuário:", font= fonte_texto, justify="center").pack(pady=10)
    entrada_usuario = tk.Entry(janela, width=25)
    entrada_usuario.pack(pady=10)

    tk.Label(janela, text="Senha:", font= fonte_texto, justify="center").pack(pady=10)
    entrada_senha = tk.Entry(janela,show="*", width=25)
    entrada_senha.pack(pady=10)

    tk.Button(janela, text="Entrar", command= lambda: tentar_login(entrada_usuario, entrada_senha, janela)).pack(pady=10)

def janela_login():
    janela = tk.Tk()

    janela.title("Janela de Login")
    centralizar_janela(janela, 500, 450)
    criar_widgets(janela)
    janela.mainloop()