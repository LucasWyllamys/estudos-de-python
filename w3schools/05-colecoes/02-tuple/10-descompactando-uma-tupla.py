# Quando criamos uma tupla, normalmente atribuímos valores a ela. Isso é chamado de "empacotamento" de uma tupla.
# Mas, em Python, também podemos extrair os valores de volta para variáveis. Isso é chamado de "descompactação":
fruits = ("apple", "banana", "cherry")  # Empacotamento

(green, yellow, red) = fruits  # Deescompactação
print(green, yellow, red)  # Saída: apple banana cherry

# Se o número de variáveis ​​for menor que o número de valores, você pode adicionar um *ao nome da variável e os valores serão atribuídos à variável como uma lista:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
# Saída: apple banana ['cherry', 'strawberry', 'raspberry']:
print(green, yellow, red)

# Se o asterisco for adicionado a outro nome de variável que não o anterior, o Python atribuirá valores à variável até que o número de valores restantes corresponda ao número de variáveis ​​restantes:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits
# Saída: apple ['mango', 'papaya', 'pineapple'] cherry:
print(green, tropic, red)
