import customtkinter

# Função de Call Back
def button_callback():
    print("botão processado!")

# Configurações iniciais
app = customtkinter.CTk()                           # Cria a janela principal.
app.title("Meu Aplicativo")                         # Define o título na janela.
app.geometry("400x150")                             # Define as dimensões da janela.
app.grid_columnconfigure(index=(0, 1), weight=1)    # Atribue o mesmo peso (1) às colunas de índice 0 e 1 (tupla).

# Criação dos controles (widgets)
btn = customtkinter.CTkButton(master=app, text="my button", command=button_callback)    # Cria um botão.
ckbox1 = customtkinter.CTkCheckBox(master=app, text="checkbox 1")     # Cria o checkbox.
ckbox2 = customtkinter.CTkCheckBox(master=app, text="checkbox 2")

# Configuração dos controles (widgets)
btn.grid(row=0, column=0, padx=20, pady=20, sticky="we", columnspan=2)  # Define a posição e o padding do widget (CTkButton, neste caso!).
ckbox1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")    
ckbox2.grid(row=1, column=1, padx= 20, pady=(0, 20), sticky="w")   # Note que o argumento pady recebe uma tupla, o que significa 0 padding na parte superior e 20 padding na parte inferior.

app.mainloop()  # Executa a root em loop.

