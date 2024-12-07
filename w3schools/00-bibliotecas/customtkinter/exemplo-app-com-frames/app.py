''' Explicação da lógica desta aplicação:
- https://customtkinter.tomschimansky.com/tutorial/frames
- https://chatgpt.com/share/675128f3-131c-8002-97fd-710220182413
'''

import customtkinter as ctk

class CheckboxFrame(ctk.CTkFrame):  # A classe CheckboxFrame herda de ctk.CTkFrame.
    # Esta classe tem por cria frames com checkboxes e retorna os rótulos dos checkboxes selecionados quando o botão é pressionado (método get).
    def __init__(self, main, title, values):   # main faz referência ao elemento pai (widget) no qual o frame será inserido (objeto App que foi passado como argumento (self) na classe App).
        super().__init__(main)   # Inicializa a classe base (ctk.CTkFrame) e conecta o frame ao widget pai (main).
        self.grid_columnconfigure(index=0, weight=1)    # Configura a grade de layout do frame para que a coluna 0 tenha peso 1 (ocupe todo o espaço horizontal disponível).
        self.values = values
        self.title = title
        self.checkboxes = []

        # Cria o label para ser o título do frame.
        self.title = ctk.CTkLabel(master=self, text=self.title, fg_color="gray30", corner_radius=6)
        # Configuração do label.
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        # Cria dinamicamente os checkboxes de acordo com os valores fornecidos na lista 'values'.
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

class RadiobuttonFrame(ctk.CTkFrame):   # A classe RadiobuttonFrame herda de ctk.CTkFrame.
    # Esta classe tem por cria frames com radiobuttons e retorna o rótulo do radiobutton selecionado quando o botão é pressionado (método get).
    def __init__(self, main, title, values):
        super().__init__(main)  # Inicializa a classe base (ctk.CTkFrame) e conecta o frame ao widget pai (main).
        self.grid_columnconfigure(index=0, weight=1)    # Configura a grade de layout do frame para que a coluna 0 tenha peso 1 (ocupe todo o espaço horizontal disponível).
        self.values = values        # Armazena a lista de valores para os botões.
        self.title = title          # Armazena o texto do título do frame.
        self.radiobuttons = []      # Lista onde serão armazenados os widgets de botões de opção criados.
        self.variable = ctk.StringVar(value="")     # Variável vinculada aos botões. Guarda o valor do botão selecionado. ctk.StringVar(value="") armazenar valores associados a widgets e sincroniza mudanças entre widgets e o programa, garantindo que qualquer alteração feita no widget (pelo usuário ou pelo código) seja refletida na variável, e vice-versa.

        # Cria o label para ser o título do frame.
        self.title = ctk.CTkLabel(master=self, text=self.title, fg_color="gray30", corner_radius=6)
        # Configuração do label.
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")    

        # Cria dinamicamente os radiobuttons de acordo com os valores fornecidos na lista 'values'.
        for i, value in enumerate(self.values):
            radiobutton = ctk.CTkRadioButton(master=self, text=value, value=value, variable=self.variable)  # text=value: Define o texto exibido ao lado do botão. value=value: Associa um valor específico ao botão. variable=self.variable: Conecta o botão à variável, garantindo que apenas um botão do grupo seja selecionado por vez.
            radiobutton.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)   # Adiciona cada botão à lista self.radiobuttons para referência futura.

    def get(self):
        return self.variable.get()  # O método get() retorna o valor atualmente selecionado nos botões de opção (armazenado na variável self.variable).
    
    def set(self, value):
        self.variable.set(value)    # O método set() permite definir o botão selecionado programaticamente, atribuindo um valor à variável self.variable.

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
        checked_checkboxes = self.frame1.get()          # Método que retorna uma lista das checkboxes marcadas no frame.     
        checked_checkboxes.extend(self.frame2.get())    # O método extend() acrescentar elementos de outra lista à lista atual.
        checked_checkboxes.append(self.frame3.get())    # O método append() adiciona o botão selecionado à lista.

        print(f"Checkboxes marcadas: {checked_checkboxes}")     # Saída: Retorna as checkboxes selecionadas.     

app = App()     # Instancia a classe (cria o objeto).
app.mainloop()  # Executa a root em loop.