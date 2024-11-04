# Você pode percorrer os itens da tupla usando um for loop:
thisTuple = ("apple", "banana", "cherry")
for x in thisTuple:
    print(x)
''' Saída: 
apple
banana
cherry
'''

# Você também pode percorrer os itens da tupla consultando seu número de índice.
# Use as funções range()e len()para criar um iterável adequado:
thisTuple = ("apple", "banana", "cherry")
for i in range(len(thisTuple)):
    print(thisTuple[i])
''' Saída: 
apple
banana
cherry
'''

# Você pode percorrer os itens da tupla usando um whileloop.
# Use a len()função para determinar o comprimento da tupla, então comece em 0 e percorra os itens da tupla consultando seus índices.
# Lembre-se de aumentar o índice em 1 após cada iteração.
thisTuple = ("apple", "banana", "cherry")
i = 0
while i < len(thisTuple):
    print(thisTuple[i])
    i += 1
''' Saída: 
apple
banana
cherry
'''
