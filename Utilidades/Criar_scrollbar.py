import tkinter as tk

def criar_scrollbar(frame: tk.Frame) -> tk.Frame:
    # Canvas com fundo igual ao frame
    canvas = tk.Canvas(frame, bg=frame["bg"], highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    # Scrollbar vertical
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame interno onde os widgets serão colocados
    frame_interno = tk.Frame(canvas, bg=frame["bg"])
    janela_id = canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    # Atualiza área de rolagem quando o conteúdo muda
    def ajustar_scroll(event):
        canvas.update_idletasks()
        bbox = canvas.bbox("all")
        if bbox:
            altura_conteudo = bbox[3] - bbox[1]
            altura_canvas = canvas.winfo_height()

            # Só define scrollregion se o conteúdo for maior que a área visível
            if altura_conteudo > altura_canvas:
                canvas.configure(scrollregion=bbox)
            else:
                # Limita o scroll exatamente à área visível
                canvas.configure(scrollregion=(0, 0, bbox[2], altura_canvas))

            canvas.itemconfig(janela_id, width=canvas.winfo_width())


    frame_interno.bind("<Configure>", ajustar_scroll)

    # Permite rolar com a roda do mouse
    def rolar(event):
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    canvas.bind_all("<MouseWheel>", rolar)

    return frame_interno
