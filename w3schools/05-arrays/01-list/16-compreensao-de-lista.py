# A compreensão de lista oferece uma sintaxe mais curta quando você deseja criar uma nova lista com base nos valores de uma lista existente.

# Exemplo: Com base em uma lista de frutas, você quer uma nova lista, contendo apenas as frutas com a letra "a" no nome.
# Sem compreensão de lista, você terá que escrever uma declaração for com um teste condicional dentro:
fruits = ['maçã', 'banana', 'morango', 'caja', 'limão']
newList = []

for x in fruits:
    if 'a' in x:
        newList.append(x)   # Adiciona o elemento se tiver a letra "a"

print(newList)  # Saída: ['maçã', 'banana', 'morango', 'caja'] (frutas que contêm a letra "a")

# Com a compreensão de lista você pode fazer tudo isso (exemplo acima) com apenas uma linha de código:
fruits = ['maçã', 'banana', 'morango', 'caja', 'limão']
newList = [x for x in fruits if 'a' in x]   # Adiciona o elemento se tiver a letra "a"

print(newList)  # Saída: ['maçã', 'banana', 'morango', 'caja'] (frutas que contêm a letra "a")

''' Sintaxe:---------------------------------------------------------------------------------------------------------------------------
newlist = [expression for item in iterable if condition == True]
O valor de retorno é uma nova lista, deixando a lista antiga inalterada.'''
''' condition-----------------------------------------
A condição é como um filtro que aceita apenas os itens que valem True.
'''
fruits = ['maçã', 'banana', 'morango', 'caja', 'limão']
newList = [x for x in fruits if x != 'maçã']    # Aceite apenas itens que não sejam "maçã" (A condição if x != "maçã" retornará Truepara todos os elementos, exceto "maçã", fazendo com que a nova lista contenha todas as frutas, exceto "maçã".)
print(newList)  # Saída: ['banana', 'morango', 'caja', 'limão']
# A condição é opcional e pode ser omitida:
fruits = ['maçã', 'banana', 'morango', 'caja', 'limão']
newList = [x for x in fruits]   # Saída: ['maçã', 'banana', 'morango', 'caja', 'limão']
''' iterable------------------------------------------
O iterável pode ser qualquer objeto iterável, como uma lista, tupla, conjunto etc.
'''
# Você pode usar a função range() para criar um iterável:
fruits = ['maçã', 'banana', 'morango', 'caja', 'limão']
newList = [x for x in range(10)]    
print(newList)      # Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Mesmo exemplo acima, mas com uma condição:
fruits = ['maçã', 'banana', 'morango', 'caja', 'limão']
newList = [x for x in range(10) if x % 2 == 0]
print(newList)      # Saída: [0, 2, 4, 6, 8]
''' expression----------------------------------------
A expressão é o item atual na iteração, mas também é o resultado, que você pode manipular antes que ele termine como um item de lista na nova lista.
'''
fruits = ['maçã', 'banana', 'morango', 'caja', 'limão']
newList = [x.upper() for x in fruits]
print(newList)  # Saída: ['MAÇÃ', 'BANANA', 'MORANGO', 'CAJA', 'LIMÃO']
# Você pode definir o resultado como quiser:
fruits = ['maçã', 'banana', 'morango', 'caja', 'limão']
newList = ['olá' for x in fruits]   # Define todos os valores na nova lista como 'olá'.
print(newList)  # Saída: ['olá', 'olá', 'olá', 'olá', 'olá']
# A expressão também pode conter condições, não como um filtro, mas como uma forma de manipular o resultado:
fruits = ['maçã', 'banana', 'morango', 'caja', 'limão']
newList = [x if x != 'banana' else 'laranja' for x in fruits]   # Retorne "laranja" em vez de "banana" (Retorne o item se não for banana, se for banana retorne laranja.)
print(newList)  # Saída: ['maçã', 'laranja', 'morango', 'caja', 'limão']



