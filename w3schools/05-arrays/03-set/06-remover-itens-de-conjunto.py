# Para remover um item de um conjunto, use o método remove() ou discard().

# Se o item a ser removido não existir, remove() vai retornar um erro:
thisSet = {"apple", "banana", "cherry"}

thisSet.remove("banana")

print(thisSet)  # Saída: {'apple', 'cherry'}

# Se o item a ser removido não existir, discard() NÃO vai retornar um erro:
thisSet = {"apple", "banana", "cherry"}

thisSet.discard("banana")

print(thisSet)  # Saída: {'apple', 'cherry'}

# Você também pode usar o método pop() para remover um item, mas esse método removerá um item aleatório, então você não pode ter certeza de qual item será removido.
# O valor de retorno do método pop() é o item removido:
thisSet = {"apple", "banana", "cherry"}

x = thisSet.pop()

print(x)        # Retorna o item removido de forma aleatória.
print(thisSet)  # Retorna o conjunto com valores restantes em ordem aleatória.
