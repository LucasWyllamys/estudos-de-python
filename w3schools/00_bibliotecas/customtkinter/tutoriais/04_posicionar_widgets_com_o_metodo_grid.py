import customtkinter as ctk

ctk.set_appearance_mode("dark")             # Modifica o modo (dark, light)
ctk.set_default_color_theme("dark-blue")    # Modifica o tema (blue, green, dark-blue)
app = ctk.CTk()                 # Instancia a classe.
app.geometry("700x400")         # Define as dimensões da aplicação.
app.title("Meu App")            # Define o título.

btn1 = ctk.CTkButton(master=app, text="Botão 1")
btn1.grid(row=0, column=0)       # O método grid() posiciona o widget em relação as colunas do seu widget pai.

btn2 = ctk.CTkButton(master=app, text="Botão 2")
btn2.grid(row=1, column=0)       # O método grid() posiciona o widget em relação as colunas do seu widget pai.

btn3 = ctk.CTkButton(master=app, text="Botão 3")
btn3.grid(row=0, column=1)       # O método grid() posiciona o widget em relação as colunas do seu widget pai.

btn4 = ctk.CTkButton(master=app, text="Botão 4")
btn4.grid(row=1, column=1)       # O método grid() posiciona o widget em relação as colunas do seu widget pai.

app.mainloop()                  # Executa o loop.