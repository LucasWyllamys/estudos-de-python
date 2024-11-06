# Um dicionário pode conter dicionários, isso é chamado de dicionários aninhados:
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

print(myFamily)
# Saída: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2001}}

# Cria três dicionários e, em seguida, crie um dicionário que conterá os outros três dicionários:
child1 = {
    "name": "Emil",
    "year": 2004
}

child2 = {
    "name": "Tobias",
    "year": 2007
}

child3 = {
    "name": "Linus",
    "year": 2001
}

myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myFamily)
# Saída: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2001}}
