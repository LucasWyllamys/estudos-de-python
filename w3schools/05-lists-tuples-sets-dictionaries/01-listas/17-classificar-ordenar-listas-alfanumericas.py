# Classificar em ordem crescente:------------------------------------------------------------------------------------

# Objetos de lista têm um método sort() que classificará a lista alfanumericamente, em ordem crescente, por padrão:
myList = ['morango', 'limão', 'pera', 'uva', 'banana', 'laranja']
myList.sort()
print(myList)   # Saída: ['banana', 'laranja', 'limão', 'morango', 'pera', 'uva']
# Classifique a lista numericamente:
myList = [100, 50, 65, 82, 23]
myList.sort()
print(myList)   # Saída: [23, 50, 65, 82, 100]

# Classificar em ordem decrescente:----------------------------------------------------------------------------------

# Para classificar em ordem decrescente, use o argumento de palavra-chave reverse = True:
myList = ['morango', 'limão', 'pera', 'uva', 'banana', 'laranja']
myList.sort(reverse = True)
print(myList)   # Saída: ['uva', 'pera', 'morango', 'limão', 'laranja', 'banana']
# Classifique em ordem decrescente a lista numericamente:
myList = [100, 50, 65, 82, 23]
myList.sort(reverse = True)
print(myList)   # Saída: [100, 82, 65, 50, 23]

# Personalizar função de classificação:
# Você também pode personalizar sua própria função usando o argumento de palavra-chave .key = function
# A função retornará um número que será usado para classificar a lista (o menor número primeiro):
# Classifique a lista com base na proximidade do número de 50:
def myFunc(n):
    return abs(n - 50)

myList = [100, 50, 65, 82, 23]
myList.sort(key = myFunc)
print(myList)   # Saída: [50, 65, 23, 82, 100]

# Classificação sem distinção entre maiúsculas e minúsculas
# Por padrão, o sort()método diferencia maiúsculas de minúsculas, resultando em todas as letras maiúsculas sendo classificadas antes das letras minúsculas.
# A classificação com distinção entre maiúsculas e minúsculas pode gerar um resultado inesperado:
myList = ['banana', 'Laranja', 'Kiwi', 'morango']
myList.sort()
print(myList)   # Saída: ['Kiwi', 'Laranja', 'banana', 'morango'] (classifica primeiro as maiúsculas!)
# Felizmente, podemos usar funções integradas como funções-chave ao classificar uma lista.]
# Então, se você quiser uma função de classificação que não diferencia maiúsculas de minúsculas, use str.lower como uma função-chave.
# Execute uma classificação da lista que não diferencia maiúsculas de minúsculas:
myList = ['banana', 'Laranja', 'Kiwi', 'morango']
myList.sort(key = str.lower)    # str.lower tranforma, internamente, todos os elementos da lista em maiúsculas.
print(myList)   # Saída: ['banana', 'Kiwi', 'Laranja', 'morango']

# Ordem inversa: E se você quiser inverter a ordem de uma lista, independentemente do alfabeto?
# O método reverse() inverte a ordem de classificação atual dos elementos.
# Inverta a ordem dos itens da lista:
myList = ['banana', 'Laranja', 'Kiwi', 'morango']
myList.reverse()
print(myList)   # Saída: ['morango', 'Kiwi', 'Laranja', 'banana'] (a lista fica de trás para a frente!)