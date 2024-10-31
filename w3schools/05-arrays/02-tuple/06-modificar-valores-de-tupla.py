'''
Uma vez que uma tupla é criada, você não pode alterar seus valores. Tuplas são inalteráveis , ou imutáveis ​​como também são chamadas.
Mas há uma solução alternativa. Você pode converter a tupla em uma lista, alterar a lista e converter a lista de volta em uma tupla:
'''
x = ("apple", "banana", "cherry")   # Criação da tuple.
# Usa a função construtora list() para converter a tuple x na list y:
y = list(x)
y[1] = "kiwi"   # Modifica o valor na list y.
# Usa a função construtora tuple() para converter a list y na tuple x:
x = tuple(y)

print(x)  # Saída: ('apple', 'kiwi', 'cherry')
