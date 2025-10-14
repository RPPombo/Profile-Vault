from Janelas.Janela_login import janela_login
import os

print("Iniciando app!")

# Verificando a existência das pastas de dados
if not os.path.exists("./Dados"):
    os.makedirs("./Dados")

if not os.path.exists("./Dados/Contas"):
    os.makedirs("./Dados/Contas")

# Criando os arquivos de dados com templates pré-carregados
if not os.path.exists("./Dados/Logins.json"):
    with open(file="./Dados/Logins.json", mode="w+", encoding="UTF-8") as arq:
        arq.write('''[
    { "usuário": "Exemplo","email": "email@exemplo.com","senha": "123456","celular": "xx xxxxx-xxxx"}
]''')

if not os.path.exists("./Dados/Contas/Exemplo.json"):
    with open(file="./Dados/Contas/Exemplo.json", mode="w+", encoding="UTF-8") as arq:
        arq.write('''[
    {"conta": "exemplo 1","usuário": "exemplo.user","email": "email1@exemplo.com","senha": "123456","autenticação 2 fatores": "celular","site": "https://exemplo1.com.br"}
]''')

janela_login()
print("Fechando app!")