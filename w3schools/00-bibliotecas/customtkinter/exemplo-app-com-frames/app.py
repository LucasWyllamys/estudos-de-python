''' Explicação da lógica desta aplicação:
- https://customtkinter.tomschimansky.com/tutorial/frames
- https://chatgpt.com/share/675128f3-131c-8002-97fd-710220182413
'''

import customtkinter

class Frame1(customtkinter.CTkFrame):
    def __init__(self, main):   # main faz referência ao elemento pai (widget) no qual o frame será inserido (objeto App que foi passado como argumento (self) na classe App).
        super().__init__(main)

        # Criação dos controles (widgets)
        self.ckbox1 = customtkinter.CTkCheckBox(master=self, text="checkbox 1")     # self faz referência ao frame.
        self.ckbox2 = customtkinter.CTkCheckBox(master=self, text="checkbox 2")
        self.ckbox3 = customtkinter.CTkCheckBox(master=self, text="checkbox 3")

        # Configuração dos controles (widgets)
        self.ckbox1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.ckbox2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.ckbox3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

class App(customtkinter.CTk):   # ctk.CTk é a aplicação e é a classe pai
    def __init__(self):
        super().__init__()  # Herda métodos e propriedades da classe pai.

        # Configurações iniciais na root
        self.title("Meu Aplicativo")    # Especifica o título.
        self.geometry("400x180")    # Especifica as dimensões da aplicação.
        self.grid_columnconfigure(0, weight=1)  # Atribui peso 1 para a coluna 0.
        self.grid_rowconfigure(0, weight=1) # Atribui peso 1 para as linhas 0 e 1.

        # Criação dos frames
        self.frame1 = Frame1(self)  # self (referindo-se ao objeto da classe App, que herda de CTk) é passado como argumento. Isso indica que Frame1 será um filho do aplicativo principal (app).

        # Configuração dos frames
        self.frame1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        # Criação dos controles (widgets)
        self.bnt = customtkinter.CTkButton(master=self, text="meu botão", command=self.btn_callback)

        # Configuração dos controles (widgets)
        self.bnt.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    # Método de Callback do botão (executa a ação quando o botão é pressionado)
    def btn_callback(self):
        print("botão processado!")

app = App()     # Instancia a classe (cria o objeto).
app.mainloop()  # Executa a root em loop.