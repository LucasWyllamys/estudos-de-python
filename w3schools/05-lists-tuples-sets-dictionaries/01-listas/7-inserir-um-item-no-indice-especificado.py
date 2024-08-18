# Para inserir um novo item de lista, sem substituir nenhum dos valores existentes, podemos usar o método insert().
# O método insert() insere um item no índice especificado:
myList = ['maçã', 'banana', 'morango']
myList.insert(2, 'melão')   # Insere o item no índice especificado, os itens seguintes são realocados.
print(myList)               # Saída: ['maçã', 'banana', 'melão', 'morango']
