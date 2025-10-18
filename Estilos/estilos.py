def carregar_tema(tema: str) -> dict:
    if tema == "Light":
        return {
            "fonte_titulo": ("Times New Roman", 22, "bold"),
            "fonte_texto": ("Times New Roman", 14),
            "cor_bg1": "#ffffff",       # fundo principal
            "cor_bg2": "#f0f0f0",       # fundo secundário
            "cor_botao1": "#4CAF50",    # botão normal
            "cor_botao2": "#45a049",    # botão ativo
            "cor_aviso": "#af0101"      # mensagens de erro
        }

    elif tema == "Dark":
        return {
            "fonte_titulo": ("Consolas", 22, "bold"),
            "fonte_texto": ("Consolas", 14),
            "cor_bg1": "#1e1e1e",
            "cor_bg2": "#2d2d2d",
            "cor_botao1": "#81c784",
            "cor_botao2": "#66bb6a",
            "cor_aviso": "#ef5350"
        }

    elif tema == "Blue":
        return {
            "fonte_titulo": ("Verdana", 22, "bold"),
            "fonte_texto": ("Verdana", 14),
            "cor_bg1": "#e3f2fd",
            "cor_bg2": "#bbdefb",
            "cor_botao1": "#1976d2",
            "cor_botao2": "#1565c0",
            "cor_aviso": "#d32f2f"
        }

    elif tema == "Purple":
        return {
            "fonte_titulo": ("Segoe UI", 22, "bold"),
            "fonte_texto": ("Segoe UI", 14),
            "cor_bg1": "#f3e5f5",
            "cor_bg2": "#e1bee7",
            "cor_botao1": "#8e24aa",
            "cor_botao2": "#7b1fa2",
            "cor_aviso": "#c62828"
        }