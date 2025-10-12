import tkinter as tk
import pandas as pd
from Utilidades.Centralizar_janela import centralizar_janela
from Estilos.estilos import *

# -----Botões-----
def adicionar_conta(janela: tk.Tk, df: pd.DataFrame):
    janela_adicao = tk.Toplevel(janela)
    janela_adicao.title("Adicionar Conta")
    centralizar_janela(janela_adicao, 500, 600)
    janela_adicao.configure(bg=cor_branco1)

    entradas = {}

    tk.Label(janela_adicao, text="Adicionar Conta", font=fonte_titulo, bg=cor_branco2).pack(pady=20)
    tk.Label(janela_adicao, text="Caso a conta não possua alguma das colunas, deixar em branco!", font= fonte_texto, bg=cor_branco2).pack(pady=10)

    for campo in ["Conta", "Usuário", "Email", "Senha", "Autenticação 2 Fatores", "Site"]:
        tk.Label(janela_adicao, text=f"{campo}:", font=fonte_texto, bg=cor_branco2).pack(pady=5)
        entrada = tk.Entry(janela_adicao, width=25, font=fonte_texto)
        entrada.pack(pady=5)
        entradas[campo.lower()] = entrada

    def adicionar():
        nova_linha = {chave: entradas[chave].get() for chave in entradas}
        df.loc[len(df)] = nova_linha
        carregar_frame_direita(janela)
        janela_adicao.destroy()

    tk.Button(janela_adicao, text="Adicionar", font=fonte_texto, bg=cor_verde1, activebackground=cor_verde2, width=15,
        command=adicionar).pack(pady=20)
    
# -----Frames-----
def carregar_frame_esquerda(janela: tk.Tk):
    # Conta acessada do app
    tk.Label(janela.frame_esquerda, text=f"Conta:{usuario_acessado}", font=fonte_titulo, bg=cor_branco2).pack(pady=20)

    # Botões de ações
    tk.Button(janela.frame_esquerda, text="Adicionar Perfil", font=fonte_texto, bg=cor_verde1, activebackground= cor_verde2, width=15,
               command=lambda: adicionar_conta()).pack(pady=20)
    
    
def carregar_frame_direita(janela: tk.Tk):

# -----Elementos da janela-----
def criar_frames_vault(janela: tk.Tk, df: pd.DataFrame):
    janela.frame_esquerda = tk.Frame(janela, width=300)
    janela.frame_esquerda.grid(column=0, row= 0, sticky="nsew")

    janela.frame_direita = tk.Frame(janela, width=700)
    janela.frame_direita.grid(column=1, row=0, sticky="nsew")
    
# -----Criar janela-----
def janela_contas(usuario: str):
    global usuario_acessado
    usuario_acessado = usuario

    df_usuario = pd.read_json(f"./Dados/Contas{usuario}.json")

    janela = tk.Tk()
    janela.title("Profile Vault")
    centralizar_janela(janela, 1000, 800)
    criar_frames_vault(janela, df_usuario)
    janela.mainloop()
