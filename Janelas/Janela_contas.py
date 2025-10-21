import tkinter as tk
import pandas as pd
import re
from Utilidades.Centralizar_janela import centralizar_janela
from Utilidades.Salvar_json import salvar_json
from Utilidades.Criar_scrollbar import criar_scrollbar
from Classes.Usuario import Usuario
from Estilos.estilos import *

# -----Botões-----
def adicionar_perfil(janela: tk.Tk, df: pd.DataFrame):
    janela_adicao = tk.Toplevel(janela)
    janela_adicao.title("Adicionar Perfil")
    centralizar_janela(janela_adicao, 500, 700)
    janela_adicao.configure(bg=tema["cor_bg1"])

    entradas = {}

    tk.Label(janela_adicao, text="Adicionar Conta", font=tema["fonte_titulo"], bg=tema["cor_bg2"]).pack(pady=20)
    tk.Label(janela_adicao, text="Caso a conta não possua alguma das colunas, deixar em branco!", font= tema["fonte_texto"], bg=tema["cor_bg2"]).pack(pady=10)

    for campo in ["Conta", "Usuário", "Email", "Senha", "Autenticação 2 Fatores", "Site"]:
        tk.Label(janela_adicao, text=f"{campo}:", font=tema["fonte_texto"], bg=tema["cor_bg2"]).pack(pady=5)
        entrada = tk.Entry(janela_adicao, width=25, font=tema["fonte_texto"], bg=tema["cor_bg2"])
        entrada.pack(pady=5)
        entradas[campo.lower()] = entrada

    def adicionar():
        nova_linha = {chave: entradas[chave].get() for chave in entradas}
        df.loc[len(df)] = nova_linha
        salvar_json(usuario_acessado.arquivo, df)
        carregar_frame_direita(janela, df)
        janela_adicao.destroy()

    tk.Button(janela_adicao, text="Adicionar", font=tema["fonte_texto"], bg=tema["cor_botao1"], activebackground=tema["cor_botao2"], width=15,
        command=adicionar).pack(pady=20)
    
def editar_perfil(janela: tk.Tk, df: pd.DataFrame):
    janela_edicao = tk.Toplevel(janela)
    janela_edicao.title("Editar Perfil")
    centralizar_janela(janela_edicao, 500, 700)
    janela_edicao.configure(bg=tema["cor_bg1"])

    tk.Label(janela_edicao, text="Índice do perfil:", font=tema["fonte_titulo"], bg=tema["cor_bg2"]).pack(pady=20)
    entrada_indice = tk.Entry(janela_edicao, font=tema["fonte_texto"], bg=tema["cor_bg2"], width=25)
    entrada_indice.pack(pady=5)

    def selecionar():
        if entrada_indice.get().strip() != "":
            try:
                indice = int(entrada_indice.get().strip())

                # Verifica se o índice existe
                if indice not in df.index:
                    raise KeyError

                for widget in janela_edicao.winfo_children():
                    widget.destroy()

                entradas = {}

                tk.Label(janela_edicao, text="Editar Perfil:", font=tema["fonte_titulo"], bg=tema["cor_bg2"]).pack(pady=20)

                for campo in df.columns:
                    tk.Label(janela_edicao, text=f"{campo.capitalize()}:", font=tema["fonte_texto"], bg=tema["cor_bg2"]).pack(pady=5)
                    entrada = tk.Entry(janela_edicao, width=25, font=tema["fonte_texto"], bg=tema["cor_bg2"])
                    entrada.pack(pady=5)
                    entrada.insert(0, str(df.at[indice, campo]))
                    entradas[campo] = entrada

                def editar():
                    for campo, entry in entradas.items():
                        df.at[indice, campo] = entry.get()
                        
                    salvar_json(usuario_acessado.arquivo, df)
                    carregar_frame_direita(janela, df)
                    janela_edicao.destroy()

                tk.Button(janela_edicao, text="Editar", font=tema["fonte_texto"], bg=tema["cor_botao1"], activebackground=tema["cor_botao2"], width=15,
                    command=editar).pack(pady=20)

            except (ValueError, KeyError):
                tk.Label(janela_edicao, text="Preencha com um índice válido!", font=tema["fonte_texto"], fg=tema["cor_aviso"], bg=tema["cor_bg2"]).pack(pady=10)
        else:
            tk.Label(janela_edicao, text="Preencha o campo corretamente!", font=tema["fonte_texto"], fg=tema["cor_aviso"], bg=tema["cor_bg2"]).pack(pady=10)

    tk.Button(janela_edicao, text="Selecionar", font=tema["fonte_texto"], bg=tema["cor_botao1"], activebackground=tema["cor_botao2"], width=15, 
              command=selecionar).pack(pady=20)
    
def configuracoes(janela: tk.Tk, df: pd.DataFrame):
    janela_config = tk.Toplevel(janela)
    janela_config.title("Configurações")
    centralizar_janela(janela_config, 500, 800)
    janela_config.configure(bg=tema["cor_bg1"])

    tk.Label(janela_config, text="Configurações", bg=tema["cor_bg2"], font=tema["fonte_titulo"]).pack(pady=20)

    tk.Label(janela_config, text="Insira a nova senha:", bg=tema["cor_bg2"], font=tema["fonte_texto"]).pack(pady=10)
    entrada_senha1 = tk.Entry(janela_config, show="*", font=tema["fonte_texto"], bg=tema["cor_bg2"])
    entrada_senha1.pack(pady=10)

    tk.Label(janela_config, text="Confirme a nova senha:", bg=tema["cor_bg2"], font=tema["fonte_texto"]).pack(pady=10)
    entrada_senha2 = tk.Entry(janela_config, show="*", font=tema["fonte_texto"], bg=tema["cor_bg2"])
    entrada_senha2.pack(pady=10)


    def alterar_senha():
        if entrada_senha1.get().strip() == "" or entrada_senha2.get().strip() == "":
            aviso_senha["text"] = "Preencha todos os campos!"
            aviso_senha["fg"] = tema["cor_aviso"]
        elif entrada_senha1.get().strip() != entrada_senha2.get().strip():
            aviso_senha["text"] = "As senhas não são iguais!"
            aviso_senha["fg"] = tema["cor_aviso"]
        else:
            usuario_acessado.senha = entrada_senha2.get().strip()
            aviso_senha["text"] = "Senha alterada com sucesso!"
            aviso_senha["fg"] = tema["cor_botao1"]

    tk.Button(janela_config, text="Alterar senha", font=tema["fonte_texto"], bg=tema["cor_botao1"], activebackground=tema["cor_botao2"], width=15,
              command=alterar_senha).pack(pady=10)
    
    global aviso_senha
    aviso_senha = tk.Label(janela_config, text="", font=tema["fonte_texto"], bg=tema["cor_bg2"])
    aviso_senha.pack(pady=(0, 5))

    tk.Label(janela_config, text="Insira a novo celular(formato: +xx xx xxxxx-xxxx):", bg=tema["cor_bg2"], font=tema["fonte_texto"]).pack(pady=10)
    entrada_celular = tk.Entry(janela_config, font=tema["fonte_texto"], bg=tema["cor_bg2"])
    entrada_celular.pack(pady=10)

    def alterar_celular():
        celular = entrada_celular.get().strip()
        padrao = r"^\+\d{2} \d{2} \d{5}-\d{4}$"
        if celular == "":
            aviso_celular["text"] = "Preencha o campo do celular!"
            aviso_celular["fg"] = tema["cor_aviso"]
        elif not re.match(padrao, celular):
            aviso_celular["text"] = "Formato inválido! Use: +xx xx xxxxx-xxxx"
            aviso_celular["fg"] = tema["cor_aviso"]
        else:
            usuario_acessado.celular = celular
            aviso_celular["text"] = "Celular atualizado com sucesso!"
            aviso_celular["fg"] = tema["cor_botao1"]

    tk.Button(janela_config, text="Alterar celular", font=tema["fonte_texto"], bg=tema["cor_botao1"], activebackground=tema["cor_botao2"], width=15,
              command=alterar_celular).pack(pady=10)
    
    global aviso_celular
    aviso_celular = tk.Label(janela_config, text="", font=tema["fonte_texto"], bg=tema["cor_bg2"])
    aviso_celular.pack(pady=(0, 5))
    

    tk.Label(janela_config, text="Alterar o tema:", font=tema["fonte_texto"], bg=tema["cor_bg2"]).pack(pady=10)

    def alterar_tema(novo_tema: str):
        global tema
        usuario_acessado.tema = novo_tema
        tema = carregar_tema(novo_tema)
        carregar_frame_esquerda(janela, df)
        carregar_frame_direita(janela, df)

    tema_var = tk.StringVar(value=usuario_acessado.tema)

    tk.Radiobutton(janela_config, text="Light", font=tema["fonte_texto"],bg=tema["cor_bg2"],
               variable=tema_var, value="Light",
               command=lambda: alterar_tema("Light")).pack()

    tk.Radiobutton(janela_config, text="Dark", font=tema["fonte_texto"],bg=tema["cor_bg2"],
                variable=tema_var, value="Dark",
                command=lambda: alterar_tema("Dark")).pack()

    tk.Radiobutton(janela_config, text="Blue", font=tema["fonte_texto"],bg=tema["cor_bg2"],
                variable=tema_var, value="Blue",
                command=lambda: alterar_tema("Blue")).pack()

    tk.Radiobutton(janela_config, text="Purple", font=tema["fonte_texto"], bg=tema["cor_bg2"],
                variable=tema_var, value="Purple",
                command=lambda: alterar_tema("Purple")).pack()


# -----Frames-----
def carregar_frame_esquerda(janela: tk.Tk, df: pd.DataFrame):
    janela.frame_esquerda.configure(bg=tema["cor_bg1"])
    for widget in janela.frame_esquerda.winfo_children():
        widget.destroy()

    # Conta acessada do app
    tk.Label(janela.frame_esquerda, text=f"Conta:{usuario_acessado.nome}", font=tema["fonte_titulo"], bg=tema["cor_bg2"]).pack(pady=20)

    # Botões de ações
    tk.Button(janela.frame_esquerda, text="Adicionar Perfil", font=tema["fonte_texto"], bg=tema["cor_botao1"], activebackground= tema["cor_botao2"], width=15,
               command=lambda: adicionar_perfil(janela, df)).pack(pady=20)
    tk.Button(janela.frame_esquerda, text="Editar Perfil", font=tema["fonte_texto"], bg=tema["cor_botao1"], activebackground= tema["cor_botao2"], width=15,
               command=lambda: editar_perfil(janela, df)).pack(pady=20)
    tk.Button(janela.frame_esquerda, text="Configurações", font=tema["fonte_texto"], bg=tema["cor_botao1"], activebackground= tema["cor_botao2"], width=15,
               command=lambda: configuracoes(janela, df)).pack(pady=20)
    
    
def carregar_frame_direita(janela: tk.Tk, df: pd.DataFrame):
    janela.frame_direita.configure(bg=tema["cor_bg1"])
    for widget in janela.frame_direita.winfo_children():
        widget.destroy()

    frame_interno = criar_scrollbar(janela.frame_direita)
    nomes_colunas = ["Index", "Conta", "Usuário", "Email", "Senha", "Autenticação 2 fatores", "Site"]
    colunas = []

    # Permitir expansão das colunas
    for i in range(len(nomes_colunas)):
        frame_interno.grid_columnconfigure(i, weight=1)

    # Criar frames de colunas
    for i, nome in enumerate(nomes_colunas):
        coluna_frame = tk.Frame(frame_interno, width=200, bg=tema["cor_bg1"])
        coluna_frame.grid(column=i, row=0, sticky="nsew", padx=2, pady=2)
        colunas.append(coluna_frame)
        tk.Label(coluna_frame, text=nome, font=tema["fonte_texto"], bg=tema["cor_bg2"]).pack(pady=10)

    # Preencher dados
    if df is not None and not df.empty:
        for i, linha in df.iterrows():
            for coluna_frame, nome_coluna in zip(colunas, nomes_colunas):
                valor = str(i) if nome_coluna.lower() == "index" else str(linha.get(nome_coluna.lower(), ""))
                tk.Label(coluna_frame, text=valor, font=tema["fonte_texto"], bg=tema["cor_bg2"]).pack(pady=5)

    
# -----Elementos da janela-----
def criar_frames_vault(janela: tk.Tk):
    # Permitir expansão dos frames
    janela.grid_rowconfigure(0, weight=1)
    janela.grid_columnconfigure(0, weight=1)
    janela.grid_columnconfigure(1, weight=3)

    janela.frame_esquerda = tk.Frame(janela, width=300)
    janela.frame_esquerda.grid(column=0, row=0, sticky="nsew")

    janela.frame_direita = tk.Frame(janela, width=1400)
    janela.frame_direita.grid(column=1, row=0, sticky="nsew")

# -----Criar janela-----
def janela_contas(usuario: Usuario):
    global usuario_acessado
    usuario_acessado = usuario    

    colunas = ["conta", "usuário", "email", "senha", "autenticação 2 fatores", "site"]

    df_usuario = pd.read_json(usuario_acessado.arquivo)

    if list(df_usuario.columns) !=  colunas: 
        df_usuario = pd.DataFrame(columns=colunas)

    janela = tk.Tk()
    janela.title("Profile Vault")
    centralizar_janela(janela, 1700, 800)
    global tema
    tema = carregar_tema(usuario_acessado.tema)
    criar_frames_vault(janela)
    carregar_frame_esquerda(janela, df_usuario)
    carregar_frame_direita(janela, df_usuario)
    janela.mainloop()
