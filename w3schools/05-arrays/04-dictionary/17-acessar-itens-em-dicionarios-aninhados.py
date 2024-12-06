# Para acessar itens de um dicionário aninhado, use o nome dos dicionários, começando pelo dicionário externo:
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

print(myFamily["child2"]["name"])   # Saída: Tobias
