# Você pode usar o método extend(), cujo objetivo é adicionar elementos de uma lista a outra:
lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]

lista1.extend(lista2)
print(lista1)   # Saída: ['a', 'b', 'c', 1, 2, 3]

# Outra maneira de unir duas listas é anexar todos os itens da lista2 na lista1, um por um:
lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]

for x in lista2:
    lista1.append(x)

print(lista1)   # Saída: ['a', 'b', 'c', 1, 2, 3]

# Você pode juntar duas ou mais listas usando o operador +, cria uma nova lista com o resltado da junção.
lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]

lista3 = lista1 + lista2
print(lista3)   # Saída: ['a', 'b', 'c', 1, 2, 3]



