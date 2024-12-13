# Adicionar um item ao dicionário é feito usando uma nova chave de índice e atribuindo um valor a ela:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisDict["color"] = "red"
print(thisDict)
# Saída: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# O método update() atualizará o dicionário com os itens de um argumento fornecido. Se o item não existir, o item será adicionado.
# O argumento deve ser um dicionário ou um objeto iterável com pares chave:valor.
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisDict.update({"color": "red"})
print(thisDict)
# Saída: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
