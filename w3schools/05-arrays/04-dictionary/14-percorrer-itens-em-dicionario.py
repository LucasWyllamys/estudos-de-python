# Você pode percorrer um dicionário usando um for loop.
# Ao percorrer um dicionário, o valor de retorno são as chaves do dicionário, mas também existem métodos para retornar os valores.

# Imprime todos os nomes de chaves no dicionário, um por um:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in thisDict:
    print(x)
''' Saída:
brand
model
year
'''

# Você pode usar o método keys() para retornar as chaves de um dicionário:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in thisDict.keys():
    print(x)
''' Saída:
brand
model
year
'''

# Imprime todos os valores no dicionário, um por um:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in thisDict:
    print(thisDict[x])
''' Saída:
Ford
Mustang
1964
'''

# Você também pode usar o método values() para retornar valores de um dicionário:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in thisDict.values():
    print(x)
''' Saída:
Ford
Mustang
1964
'''

# Você pode fazer um loop por chaves e valores usando o método items():
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x, y in thisDict.items():
    print(x, y)
''' Saída:
brand Ford
model Mustang
year 1964
'''
