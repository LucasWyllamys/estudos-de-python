import customtkinter as ctk

# Configurações da aplicação
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("400x220")
app.grid_columnconfigure(index=(0, 1), weight=1)
app.grid_rowconfigure(index=0, weight=1)

# Frame 1
frame1 = ctk.CTkFrame(master=app)
frame1.grid_columnconfigure(index=0, weight=1)
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
# Frame 2
frame2 = ctk.CTkScrollbar(master=app)
frame2.grid_columnconfigure(index=0, weight=1)
frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Label 1
label1 = ctk.CTkLabel(master=frame1, text="Label 1")
label1.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
# Label 2
label2 = ctk.CTkLabel(master=frame2, text="Label 2")
label2.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

app.mainloop()

