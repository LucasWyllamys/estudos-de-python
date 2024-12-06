# O método pop() remove o item com o nome de chave especificado:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisDict.pop("model")
print(thisDict)  # Saída: {'brand': 'Ford', 'year': 1964}

# O método popitem() remove o último item inserido (em versões anteriores à 3.7, um item aleatório é removido):
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisDict.popitem()
print(thisDict)  # Saída: {'brand': 'Ford', 'model': 'Mustang'}

# A palavra-chave del remove o item com o nome de chave especificado:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

del thisDict["model"]
print(thisDict)  # Saída: {'brand': 'Ford', 'year': 1964}
