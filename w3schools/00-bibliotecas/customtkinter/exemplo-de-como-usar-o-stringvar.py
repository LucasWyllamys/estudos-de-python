'''
- StringVar(): Método que armazena valores associados a widgets e sincroniza mudanças entre widgets e o programa, garantindo que qualquer alteração feita no widget (pelo usuário ou pelo código) seja refletida na variável, e vice-versa.
- trace("w", callback): Permite monitorar mudanças na variável e executar uma função automaticamente quando isso ocorre.
    - "w" indica que o evento será disparado quando o valor for alterado (escrito = write).
    - callback é a função que será executada.
'''

import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Exemplo de StringVar")
        self.grid_columnconfigure(index=(0, 1), weight=1)
        self._set_appearance_mode("dark")   # Modos: "dark", "light"
        ctk.set_default_color_theme("green") # Opções de temas: "blue", "dark-blue", "green"

        # Variável de controle
        self.var = ctk.StringVar(value="Texto inicial")

        # Campo de entrada
        self.entry = ctk.CTkEntry(master=self, textvariable=self.var)
        self.entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        # Botão para alterar o valor programaticamente
        self.change_button = ctk.CTkButton(master=self, text="Alterar Texto", command=self.change_text)
        self.change_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Botão para mostrar o valor atual
        self.show_button = ctk.CTkButton(master=self, text="Mostrar Texto", command=self.show_text)
        self.show_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Adiciona um trace
        self.var.trace(mode="w", callback=self.on_change)

    def change_text(self):
        self.var.set("Texto alterado")

    def show_text(self):
        print("Texto atual:", self.var.get())

    def on_change(self, *args):
        print("O valor mudou para:", self.var.get())

app = App()
app.mainloop()
