import tkinter as tk
import pandas as pd
from Utilidades.Centralizar_janela import centralizar_janela
from Utilidades.Salvar_json import salvar_json
from Estilos.estilos import carregar_tema

def janela_criar_usuario(janela: tk.Tk):
    janela_criacao = tk.Toplevel(janela)
    janela_criacao.title("Criar Usuário")
    centralizar_janela(janela_criacao, 500, 700)
    tema = carregar_tema("Light")

    # Título
    tk.Label(janela_criacao, text="Criar Usuário", font=tema["fonte_titulo"], bg=tema["cor_bg2"]).pack(pady=(0, 20))

    entradas = {}

    for campo in ["usuário", "email", "senha", "celular"]:
        tk.Label(janela_criacao, text=f"{campo.capitalize()}:", font=tema["fonte_texto"],bg=tema["cor_bg2"]).pack(pady=10)
        entrada = tk.Entry(janela_criacao, font=tema["fonte_texto"], width=25, bg=tema["cor_bg2"])
        entrada.pack(pady=10)
        entradas[campo] = entrada
    
    def criar(entradas: dict):
        problema = False 
        for campo in entradas:
            if entradas[campo].get() == "":
                aviso_criar["text"] = "Preencha todos os campos!"
                aviso_criar["fg"] = tema["cor_aviso"]
                problema = True
        
        if not problema:
            df = pd.read_json("./Dados/Logins.json")

            nova_linha = {chave: entradas[chave].get() for chave in entradas}
            df.loc[len(df)] = nova_linha

            salvar_json("./Dados/Logins.json", df)

            with open(f"./Dados/Contas/{entradas["usuário"].get()}.json", mode="x") as arq:
                arq.write('''[]''')

            janela_criacao.destroy()

    tk.Button(janela_criacao, text="Criar", font=tema["fonte_texto"], bg=tema["cor_botao1"], fg=tema["cor_bg2"], activebackground=tema["cor_botao2"],width=15,
              command=lambda: criar(entradas)).pack(pady=(0,10))
    
    global aviso_criar
    aviso_criar = tk.Label(janela_criacao, text="", font=tema["fonte_texto"], bg=tema["cor_bg2"])
    aviso_criar.pack(pady=(0, 5))
