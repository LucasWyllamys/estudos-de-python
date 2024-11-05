# Você pode percorrer os itens da lista usando um for loop.
fruits = ['maçã', 'banana', 'morango']
for x in fruits:
    print(x)
''' Saída: 
maçã
banana
morango
'''

# Você também pode percorrer os itens da lista consultando seu número de índice.
# Use as funções range()e len()para criar um iterável adequado.
fruits = ['uva', 'pera', 'limão']
for i in range(len(fruits)):        # range(len(fruits)) criam "range(0, 3)"
    print(fruits[i])
''' Saída: 
uva
pera
limão
'''

''' Você pode percorrer os itens da lista usando um whileloop.
Use a len()função para determinar o comprimento da lista, comece em 0 e percorra os itens da lista consultando seus índices.
Lembre-se de aumentar o índice em 1 após cada iteração.'''
fruits = ['melão', 'açaí', 'cajá']
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1
''' Saída: 
melão
açaí
cajá
'''

# A Compreensão de Lista oferece a sintaxe mais curta para percorrer listas:
fruits = ['laranja', 'acerola', 'caju']
[print(x) for x in fruits]
''' Saída: 
laranja
acerola
caju
'''