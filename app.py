from Janelas.Janela_login import janela_login
import os

print("Inicinado app!")

if not os.path.exists("./Dados"):
    os.makedirs("./Dados")

if not os.path.exists("./Dados/Contas"):
    os.makedirs("./Dados/Contas")

janela_login()
print("Fechando app!")