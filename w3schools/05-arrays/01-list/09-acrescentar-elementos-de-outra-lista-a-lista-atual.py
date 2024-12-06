# Para acrescentar elementos de outra lista à lista atual, use o método extend().
myList = ['maçã', 'banana', 'morango']
otherList = ['manga', 'uva', 'laranja', 'pera']
myList.extend(otherList)    # Acrescenta os itens da lista "otherList" ao final da lista "myList".
print(myList)               # Saída: ['maçã', 'banana', 'morango', 'manga', 'uva', 'laranja', 'pera']

# Adicionar qualquer iterável: O método extend() não anexa apenas listas, você pode adicionar qualquer objeto iterável (tuplas, conjuntos, dicionários etc.).
myList = ['maçã', 'banana', 'morango']
myTuple = ('kiwi', 'laranja')
myList.extend(myTuple)  # Acrescenta os itens da tuple "myTuple" ao final da lista "myList".
print(myList)           # Saída: ['maçã', 'banana', 'morango', 'kiwi', 'laranja']
