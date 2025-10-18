import tkinter as tk
from Utilidades.Centralizar_janela import centralizar_janela
from Utilidades.Verificar_login import verificar_login
from Janelas.Janela_contas import janela_contas
from Janelas.Janela_reset_senha import janela_resetar_senha
from Janelas.Janela_criar_usuario import janela_criar_usuario
from Classes.Usuario import Usuario
from Estilos.estilos import carregar_tema

# -----Botões-----
def tentar_login(entrada_usuario: tk.Entry, entrada_senha: tk.Entry, janela: tk.Tk):
    usuario_dado = entrada_usuario.get().strip()
    senha_dada = entrada_senha.get().strip()

    if verificar_login(usuario_dado, senha_dada):
        janela.destroy()
        usuario = Usuario(usuario_dado)
        janela_contas(usuario)
    else:
        aviso_login["text"] = "Usuário e/ou Senha incorreto(s)!"
        aviso_login["fg"] = tema["cor_aviso"]

# -----Elementos da janela-----
def criar_widgets_login(janela: tk.Tk):
    janela.configure(bg=tema["cor_bg1"])

    # Frame principal centralizado
    frame = tk.Frame(janela, bg=tema["cor_bg2"], padx=30, pady=30, relief="raised", bd=2)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Titulo
    tk.Label(frame, text="Login", font=tema["fonte_titulo"], bg=tema["cor_bg2"]).pack(pady=(0, 20))

    # Entrada Usuário
    tk.Label(frame, text="Usuário:", font=tema["fonte_texto"], bg=tema["cor_bg2"]).pack(pady=(5, 2))
    entrada_usuario = tk.Entry(frame, width=25, font=tema["fonte_texto"], bd=2, relief="groove")
    entrada_usuario.pack(pady=(0, 10))

    # Entrada Senha
    tk.Label(frame, text="Senha:", font=tema["fonte_texto"], bg=tema["cor_bg2"]).pack(pady=(5, 2))
    entrada_senha = tk.Entry(frame, show="*", width=25, font=tema["fonte_texto"], bd=2, relief="groove")
    entrada_senha.pack(pady=(0, 20))

    # Botões
    tk.Button(frame, text="Entrar", font=tema["fonte_texto"], bg=tema["cor_botao1"], fg=tema["cor_bg2"], activebackground=tema["cor_botao2"], width=15,
              command=lambda: tentar_login(entrada_usuario, entrada_senha, janela)).pack(pady=(0, 10))

    tk.Button(frame, text="Esqueci a senha", font=tema["fonte_texto"], bg=tema["cor_botao1"], fg=tema["cor_bg2"], activebackground=tema["cor_botao2"],width=15,
              command=lambda: janela_resetar_senha(janela)).pack(pady=(0,10))
    
    tk.Button(frame, text="Criar Usuário", font=tema["fonte_texto"], bg=tema["cor_botao1"], fg=tema["cor_bg2"], activebackground=tema["cor_botao2"],width=15,
              command=lambda: janela_criar_usuario(janela)).pack(pady=(0,10))

    # Label de aviso de login
    global aviso_login
    aviso_login = tk.Label(frame, text="", font=tema["fonte_texto"], bg=tema["cor_bg2"])
    aviso_login.pack(pady=(0, 5))

# -----Criar janela-----
def janela_login():
    janela = tk.Tk()
    janela.title("Login")
    centralizar_janela(janela, 500, 450)
    global tema
    tema = carregar_tema("Light")
    criar_widgets_login(janela)
    janela.mainloop()
