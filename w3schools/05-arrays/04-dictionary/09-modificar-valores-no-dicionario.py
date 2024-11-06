# Você pode alterar o valor de um item específico consultando seu nome de chave:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisDict["year"] = 2018
print(thisDict)  # Saída: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# O método update() atualizará o dicionário com os itens do argumento fornecido.
# O argumento deve ser um dicionário ou um objeto iterável com pares chave:valor.
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisDict.update({"year": 2020})
print(thisDict)  # Saída: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
