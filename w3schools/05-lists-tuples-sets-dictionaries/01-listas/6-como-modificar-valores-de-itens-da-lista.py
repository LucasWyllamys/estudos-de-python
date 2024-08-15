# Alterar valor do item: Para alterar o valor de um item específico, consulte o número do índice.
myList = ['maçã', 'banana', 'morango']
myList[1] = 'uva'
print(myList)   # Saída: ['maçã', 'uva', 'morango']

# Alterar um intervalo de valores de itens: Para alterar o valor dos itens dentro de um intervalo específico, defina uma lista com os novos valores e consulte o intervalo de números de índice onde deseja inserir os novos valores:
myList = ['maçã', 'banana', 'morango', 'laranja', 'kiwi', 'manga']
myList[1:3] = ['limão', 'uva']
print(myList)   # Saída: ['maçã', 'limão', 'uva', 'laranja', 'kiwi', 'manga']

# Se você inserir mais itens do que substituir, os novos itens serão inseridos onde você especificou, e os itens restantes serão movidos de acordo:
myList = ['maçã','banana', 'morango']
myList[1:2] = ['limão', 'uva']
print(myList)   # Saída: ['maçã', 'limão', 'uva', 'morango'] (Obs.: 'limão' e 'uva' entraram no lugar de 'banana' e o resto foi realocado de acordo.)

# Se você inserir menos itens do que substituir, os novos itens serão inseridos onde você especificou, e os itens restantes serão movidos de acordo:
myList = ['maçã','banana', 'morango']
myList[1:3] = ['laranja']
print(myList)   # Saída: ['maçã', 'laranja'] (Obs.: altera o segundo e o terceiro valor substituíndo-as por um outro.)