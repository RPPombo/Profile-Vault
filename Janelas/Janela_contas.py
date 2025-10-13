import tkinter as tk
import pandas as pd
from Utilidades.Centralizar_janela import centralizar_janela
from Classes.Usuario import Usuario
from Estilos.estilos import *

# -----Botões-----
def adicionar_perfil(janela: tk.Tk, df: pd.DataFrame):
    janela_adicao = tk.Toplevel(janela)
    janela_adicao.title("Adicionar Perfil")
    centralizar_janela(janela_adicao, 500, 700)
    janela_adicao.configure(bg=cor_branco1)

    entradas = {}

    tk.Label(janela_adicao, text="Adicionar Conta", font=fonte_titulo, bg=cor_branco2).pack(pady=20)
    tk.Label(janela_adicao, text="Caso a conta não possua alguma das colunas, deixar em branco!", font= fonte_texto, bg=cor_branco2).pack(pady=10)

    for campo in ["Conta", "Usuário", "Email", "Senha", "Autenticação 2 Fatores", "Site"]:
        tk.Label(janela_adicao, text=f"{campo}:", font=fonte_texto, bg=cor_branco2).pack(pady=5)
        entrada = tk.Entry(janela_adicao, width=25, font=fonte_texto, bg=cor_branco2)
        entrada.pack(pady=5)
        entradas[campo.lower()] = entrada

    def adicionar():
        nova_linha = {chave: entradas[chave].get() for chave in entradas}
        df.loc[len(df)] = nova_linha
        carregar_frame_direita(janela, df)
        janela_adicao.destroy()

    tk.Button(janela_adicao, text="Adicionar", font=fonte_texto, bg=cor_verde1, activebackground=cor_verde2, width=15,
        command=adicionar).pack(pady=20)
    
def editar_perfil(janela: tk.Tk, df: pd.DataFrame):
    janela_edicao = tk.Toplevel(janela)
    janela_edicao.title("Editar Perfil")
    centralizar_janela(janela_edicao, 500, 700)
    janela_edicao.configure(bg=cor_branco1)

    tk.Label(janela_edicao, text="Índice do perfil:", font=fonte_titulo, bg=cor_branco2).pack(pady=20)
    entrada_indice = tk.Entry(janela_edicao, font=fonte_texto, bg=cor_branco2, width=25)
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

                tk.Label(janela_edicao, text="Editar Perfil:", font=fonte_titulo, bg=cor_branco2).pack(pady=20)

                for campo in df.columns:
                    tk.Label(janela_edicao, text=f"{campo.capitalize()}:", font=fonte_texto, bg=cor_branco2).pack(pady=5)
                    entrada = tk.Entry(janela_edicao, width=25, font=fonte_texto, bg=cor_branco2)
                    entrada.pack(pady=5)
                    entrada.insert(0, str(df.at[indice, campo]))
                    entradas[campo] = entrada

                def editar():
                    for campo, entry in entradas.items():
                        df.at[indice, campo] = entry.get()

                    carregar_frame_direita(janela, df)
                    janela_edicao.destroy()

                tk.Button(janela_edicao, text="Editar", font=fonte_texto, bg=cor_verde1, activebackground=cor_verde2, width=15,
                    command=editar).pack(pady=20)

            except (ValueError, KeyError):
                tk.Label(janela_edicao, text="Preencha com um índice válido!", font=fonte_texto, fg=cor_vermelho1, bg=cor_branco2).pack(pady=10)
        else:
            tk.Label(janela_edicao, text="Preencha o campo corretamente!", font=fonte_texto, fg=cor_vermelho1, bg=cor_branco2).pack(pady=10)

    tk.Button(janela_edicao, text="Selecionar", font=fonte_texto, bg=cor_verde1, activebackground=cor_verde2, width=15, 
              command=selecionar).pack(pady=20)
    
# -----Frames-----
def carregar_frame_esquerda(janela: tk.Tk, df: pd.DataFrame):
    for widget in janela.frame_esquerda.winfo_children():
        widget.destroy()

    # Conta acessada do app
    tk.Label(janela.frame_esquerda, text=f"Conta:{usuario_acessado.nome}", font=fonte_titulo, bg=cor_branco2).pack(pady=20)

    # Botões de ações
    tk.Button(janela.frame_esquerda, text="Adicionar Perfil", font=fonte_texto, bg=cor_verde1, activebackground= cor_verde2, width=15,
               command=lambda: adicionar_perfil(janela, df)).pack(pady=20)
    tk.Button(janela.frame_esquerda, text="Editar Perfil", font=fonte_texto, bg=cor_verde1, activebackground= cor_verde2, width=15,
               command=lambda: editar_perfil(janela, df)).pack(pady=20)
    
    
def carregar_frame_direita(janela: tk.Tk, df: pd.DataFrame):
    for widget in janela.frame_direita.winfo_children():
        widget.destroy()

    for coluna in df.columns:
        tk.Label(janela.frame_direita, text=df[coluna], font= fonte_texto).pack(pady=5)

# -----Elementos da janela-----
def criar_frames_vault(janela: tk.Tk):
    janela.frame_esquerda = tk.Frame(janela, width=300)
    janela.frame_esquerda.grid(column=0, row= 0, sticky="nsew")

    janela.frame_direita = tk.Frame(janela, width=700)
    janela.frame_direita.grid(column=1, row=0, sticky="nsew")
    
# -----Criar janela-----
def janela_contas(usuario: Usuario):
    global usuario_acessado
    usuario_acessado = usuario

    df_usuario = pd.read_json(usuario_acessado.arquivo)

    janela = tk.Tk()
    janela.title("Profile Vault")
    centralizar_janela(janela, 1000, 800)
    criar_frames_vault(janela)
    carregar_frame_esquerda(janela, df_usuario)
    carregar_frame_direita(janela, df_usuario)
    janela.mainloop()
