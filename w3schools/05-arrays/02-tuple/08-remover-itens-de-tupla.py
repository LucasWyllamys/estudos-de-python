# Tuplas são imutáveis, então você não pode remover itens delas, mas você pode usar a mesma solução alternativa que usamos para alterar e adicionar itens de tupla:
# Converta a tupla em uma lista, remova "apple" e converta-a novamente em uma tupla:
thisTuple = ("apple", "banana", "cherry")
y = list(thisTuple)
y.remove("apple")

thisTuple = tuple(y)
print(thisTuple)  # Saída: ('banana', 'cherry')
