# A palavra-chave del também pode excluir o dicionário completamente:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

del thisDict
print(thisDict)  # Retorna um erro, pois este dicionário não existe mais!
