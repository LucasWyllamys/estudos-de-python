import customtkinter as ctk

ctk.set_appearance_mode("dark")             # Modifica o modo (dark, light)
ctk.set_default_color_theme("dark-blue")    # Modifica o tema (blue, green, dark-blue)
app = ctk.CTk()                 # Instancia a classe.
app.geometry("700x400")         # Define as dimensões da aplicação.
app.title("Meu App")            # Define o título.

btn1 = ctk.CTkButton(master=app, width=200, height=30, text="Botão 1")
btn1.pack()                      

btn2 = ctk.CTkButton(master=app, width=200, height=30, text="Botão 2")
btn2.pack()  

btn3 = ctk.CTkButton(master=app, width=200, height=30, text="Botão 3")
btn3.pack(pady=10)  # O método pack() posiciona o widget em relação ao topo e centro do seu widget pai. Você pode modificar o posicionamento usando os atributos padx e pady.

app.mainloop()                  # Executa o loop.