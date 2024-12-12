import customtkinter as ctk

ctk.set_appearance_mode("dark")             # Modifica o modo (dark, light)
ctk.set_default_color_theme("dark-blue")    # Modifica o tema (blue, green, dark-blue)
app = ctk.CTk()                 # Instancia a classe.
app.geometry("700x400")         # Define as dimensões da aplicação.
app.title("Meu App")            # Define o título.
# app.config(background="white")
# app.resizable(False, False)     # Faz com que não consiga redimensionar o tela da aplicação.
# app.iconbitmap("favicon.ico")   # Modifica o ícone da aplicação.

app.mainloop()                  # Executa o loop.