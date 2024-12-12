import customtkinter as ctk

ctk.set_appearance_mode("dark") # Modifica o modo (dark, light)
ctk.set_default_color_theme("dark-blue")    # Modifica o tema (blue, green, dark-blue)
app = ctk.CTk()                 # Instancia a classe.
app.geometry("700x400")         # Define as dimensões da aplicação.
app.title("Meu App")            # Define o título.

btn = ctk.CTkButton(master=app, width=200, height=30, text="Botão")
btn.place(x=10, y=30)           # O método place() posiciona o widget nos eixos x e y em relação ao seu widget pai.

app.mainloop()                  # Executa o loop.