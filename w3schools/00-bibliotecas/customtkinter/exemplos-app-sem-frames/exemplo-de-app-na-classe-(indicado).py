# É altamente recomendado usar classes que herdam de CTkpara a janela principal ou CTkFramepara um frame, porque isso aumenta muito a legibilidade do código e o código se torna facilmente extensível, porque as classes podem ser facilmente distribuídas para vários arquivos.
# Exceto para pequenos programas ou testes, sempre crie classes separadas para CTk, CTkToplevelou CTkFrame. Escrever muito código de UI em um único arquivo sem usar classes é uma dor de ler e um estilo de codificação muito ruim.
import customtkinter     # Importa a biblioteca.

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()    # Especifica que esta classe (filho) herde todas as propriedades e métodos da classe pai (customtkinter.CTk).

        # Configurações iniciais na root
        self.title("Meu Aplicativo")                        # Define o título na janela.
        self.geometry("400x150")                            # Define as dimensões da janela.
        self.grid_columnconfigure(index=(0, 1), weight=1)   # Atribue o mesmo peso (1) às colunas de índice 0 e 1 (tupla).

        # Criação dos controles (widgets)
        self.bnt = customtkinter.CTkButton(master=self, text="meu botão", command=self.bnt_callback)    # O método CTkButton() cria um botão.
        self.ckbox1 = customtkinter.CTkCheckBox(master=self, text="checkbox 1")                        # O método CTkCheckBox() cria um checkbox.
        self.ckbox2 = customtkinter.CTkCheckBox(master=self, text="checkbox 2")

        # Configurações dos controles (widgets)
        self.bnt.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)  # O método grid() define a posição e o padding do widget.
        self.ckbox1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")        
        self.ckbox2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")   # Note que o argumento pady recebe uma tupla, o que significa 0 padding na parte superior e 20 padding na parte inferior.

    # Método de Callback do botão (executa a ação quando o botão é pressionado)
    def bnt_callback(self):
        print("botão processado!")

app = App()     # Instancia a classe (cria o objeto).
app.mainloop()  # Executa a root em loop.