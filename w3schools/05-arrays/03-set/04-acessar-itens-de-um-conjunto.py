# Você não pode acessar itens em um conjunto consultando um índice ou uma chave.
# Mas você pode percorrer os itens do conjunto usando um for loop:
thisSet = {"apple", "banana", "cherry"}

for x in thisSet:
    print(x)
''' Saída: 
banana
apple
cherry
'''

# Ou perguntar se um valor especificado está ou não presente em um conjunto, usando a inpalavra-chave:
thisSet = {"apple", "banana", "cherry"}

print("banana" in thisSet)      # Saída: True
print("banana" not in thisSet)  # Saída: False
