# Você pode percorrer todas as chaves e valores de dicionários aninhados usando o método items():
myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2001
    }
}

for x, obj in myFamily.items():
    print(x,)
    for y in obj:
        print(y + ':', obj[y])
''' Saída:
child1
name: Emil
year: 2004
child2
name: Tobias
year: 2007
child3
name: Linus
year: 2001
'''
