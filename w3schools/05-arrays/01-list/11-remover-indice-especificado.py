# O método pop() remove o índice especificado.
myList = ['maçã', 'banana', 'morango']
myList.pop(1)   # Remove o segundo item da lista (banana)
print(myList)   # Saída: ['maçã', 'morango']

# A palavra-chave del também remove o índice especificado.
myList = ['maçã', 'banana', 'morango']
del myList[0]   # Remove o primeiro item da lista (maçã).
print(myList)   # Saída: ['banana', 'morango']
