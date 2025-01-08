# F-string permite formatar partes selecionadas de uma string.
# Para especificar uma string como uma f-string, basta colocar um f na frente do literal da string:
txt = f"The price is 49 dollars"
print(txt)  # Saída: The price is 49 dollars

# Para formatar valores em uma f-string, adicione marcadores de posição {}. Um marcador de posição pode conter variáveis, operações, funções e modificadores para formatar o valor:
price = 59
txt = f"The price is {price} dollars"   
print(txt)  # Saída: The price is 59 dollars

# Você pode executar operações Python dentro dos espaços reservados:
txt = f"The price is {20 * 59} dollars"
print(txt)  # Saída: The price is 1180 dollars

# Você pode realizar operações matemáticas em variáveis:
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)  # Saída: The price is 73.75 dollars

# Você pode executar instruções if...else dentro dos espaços reservados:
price = 49
txt = f"Isso é muito {'caro!' if price > 50 else 'barato!'}"
print(txt)  # Saída: Isso é muito barato!

# Você pode executar funções dentro do espaço reservado:
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)  # Saída: I love APPLES

# A função não precisa ser um método interno do Python, você pode criar suas próprias funções e usá-las:
def converter(x):
    return x * 0.3048

txt = f"The plane is flying at a {converter(30000)} meter altitude."
print(txt)  # Saída: The plane is flying at a 9144.0 meter altitude.