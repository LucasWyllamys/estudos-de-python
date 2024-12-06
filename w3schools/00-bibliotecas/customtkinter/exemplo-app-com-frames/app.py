''' Explicação da lógica desta aplicação:
- https://customtkinter.tomschimansky.com/tutorial/frames
- https://chatgpt.com/share/675128f3-131c-8002-97fd-710220182413
'''

import customtkinter as ctk

class CheckboxFrame(ctk.CTkFrame):
    def __init__(self, main, title, values):   # main faz referência ao elemento pai (widget) no qual o frame será inserido (objeto App que foi passado como argumento (self) na classe App).
        super().__init__(main)
        self.grid_columnconfigure(index=0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        # Cria dinamicamente os títulos das checkboxes.
        self.title = ctk.CTkLabel(master=self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        # Cria dinamicamente checkboxes de acordo com os valores fornecido na lista 'values'.
        for i, value in enumerate(self.values):     # Itera sobre os valores da lista 'values'.
            checkbox = ctk.CTkCheckBox(master=self, text=value)     # Cria o checkbox.
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")   # Configura o checkbox.
            self.checkboxes.append(checkbox)        # Atribui os checkboxes à lista.

    def get(self):  # Métdodo para retornar as checkboxes marcadas no frame.
        checked_checkboxes = []                         # Cria uma lista vazia.
        for checkbox in self.checkboxes:                # Itera sobre os checkboxes da lista.
            if checkbox.get() == 1:                     # Verifica se o ckeckbox está marcado (0 é desmarcado).
                checked_checkboxes.append(checkbox.cget("text"))      # Adiciona o texto do checkbok na lista.
        return checked_checkboxes   # Retorna uma lista das checkboxes marcadas.

class RadiobuttonFrame(ctk.CTkFrame):
    def __ini__(self, main, title, values):
        super().__init__(main)
        self.grid_columnconfigure(index=0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")

        self.title = ctk.CTkLabel(master=self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = ctk.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()
    
    def set(self, value):
        self.variable.set(value)

class App(ctk.CTk):   # ctk.CTk é a aplicação e é a classe pai.
    def __init__(self):
        super().__init__()  # Herda métodos e propriedades da classe pai.

        # Configurações iniciais na root
        self.title("Meu Aplicativo")                            # Especifica o título.
        self.geometry("400x220")                                # Especifica as dimensões da aplicação.
        self.grid_columnconfigure(index=(0, 1), weight=1)       # Atribui peso 1 para as colunas 0 e 1.
        self.grid_rowconfigure(index=0, weight=1)               # Atribui peso 1 para a linha 0.

        # Criação (instanciamento) dos frames com controles (widgets)
        self.frame1 = CheckboxFrame(main=self, title="Frame 1", values=["checkbox 1", "checkbox 2", "checkbox 3"])  
        self.frame2 = CheckboxFrame(main=self, title="Frame 2", values=["checkbox a", "checkbox b"])
        self.frame3 = RadiobuttonFrame(main=self, title="Frame 3", values=["option 1", "option 2"])
        # Configuração dos frames
        self.frame1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.frame2.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")
        self.frame3.grid(row=0, column=2, padx=(0, 10), pady=(10, 0), sticky="nsew")

        self.bnt = ctk.CTkButton(master=self, text="meu botão", command=self.btn_callback)  # Criação do botão na aplicação
        self.bnt.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=3)     # Configuração do botão

    # Método de Callback do botão (executa a ação quando o botão é pressionado)
    def btn_callback(self): 
        checked_checkboxes = self.frame1.get()        # Método que retorna uma lista das checkboxes marcadas no frame.     
        checked_checkboxes.extend(self.frame2.get())  # O método extend() acrescentar elementos de outra lista à lista atual.
        checked_checkboxes.extend(self.frame3.get())  
        print(f"Checkboxes marcadas: {checked_checkboxes}")     # Saída: Retorna as checkboxes selecionadas.     

app = App()     # Instancia a classe (cria o objeto).
app.mainloop()  # Executa a root em loop.