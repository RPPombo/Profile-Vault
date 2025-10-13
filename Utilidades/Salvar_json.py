import pandas as pd

def salvar_json(caminho_arquivo: str, df: pd.DataFrame):
    df.to_json(caminho_arquivo, orient="records", indent= 4, force_ascii=False)