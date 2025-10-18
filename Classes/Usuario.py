import pandas as pd
from Estilos.estilos import *
from Utilidades.Salvar_json import salvar_json

class Usuario:
    def __init__(self, nome: str):
        self.__nome = nome
        
        df_logins = pd.read_json("./Dados/Logins.json")
        usuario = df_logins[df_logins["usuário"] == nome].iloc[0]
        
        self.__email = usuario["email"]
        self.__senha = usuario["senha"]
        self.__celular = usuario["celular"]
        self.__tema = usuario["tema"]
        self.__arquivo = f"./Dados/Contas/{nome}.json"

    # Nome
    @property
    def nome(self):
        return self.__nome

    # Email
    @property
    def email(self):
        return self.__email

    # Senha
    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha_nova: str):
        self.__senha = senha_nova  
        df_logins = pd.read_json("./Dados/Logins.json")
        df_logins.loc[df_logins["usuário"] == self.__nome, "senha"] = senha_nova
        salvar_json("./Dados/Logins.json", df_logins)

    # Celular
    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular_novo):
        self.__celular = celular_novo  
        df_logins = pd.read_json("./Dados/Logins.json")
        df_logins.loc[df_logins["usuário"] == self.__nome, "celular"] = celular_novo
        salvar_json("./Dados/Logins.json", df_logins)

    # Tema
    @property
    def tema(self):
        return self.__tema
    
    @tema.setter
    def tema(self, tema_novo: str):
        self.__tema = tema_novo  
        df_logins = pd.read_json("./Dados/Logins.json")
        df_logins.loc[df_logins["usuário"] == self.__nome, "tema"] = tema_novo
        salvar_json("./Dados/Logins.json", df_logins)

    # Arquivo
    @property
    def arquivo(self):
        return self.__arquivo
