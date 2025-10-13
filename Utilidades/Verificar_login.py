import pandas as pd

def verificar_login(usuario_dado: str, senha_dada: str) -> bool:
    
    try:
        usuarios = pd.read_json("./Dados/Logins.json")

        if usuario_dado in usuarios["usuário"].values:
            linha = usuarios[usuarios["usuário"] == usuario_dado]
            senha_correta = str(linha["senha"].iloc[0])

            return senha_correta == senha_dada
        else:
            return False
        
    except FileNotFoundError:
        print("Arquivo de logins não encontrado!")
        return False
    
    except Exception as e:
        print(f"Erro ao verificar o login: {e}")