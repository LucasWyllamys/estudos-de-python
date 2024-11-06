# O método keys() retornará uma lista de todas as chaves no dicionário.
# A lista de chaves é uma visualização do dicionário, o que significa que quaisquer alterações feitas no dicionário serão refletidas na lista de chaves.
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisDict.keys()
print(x)    # Saída: dict_keys(['brand', 'model', 'year'])
